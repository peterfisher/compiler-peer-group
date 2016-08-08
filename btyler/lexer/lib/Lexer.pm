package Lexer;
use 5.22.0;
use Moose;
use namespace::autoclean;
use Data::Dumper qw(Dumper);
use experimental qw(signatures postderef);

has input => (is => "rw", isa => "Str");
has state => (is => 'rw', isa => "Str");
has pos => (is => 'rw', isa => "Int", default => 0);
has total => (is => 'rw', isa => "Int", default => 0);
has start => (is => 'rw', isa => "Int", default => 0);

has emit_cb => (
    is => 'rw',
    isa => 'CodeRef',
    default => sub ($lexeme) { say Dumper($lexeme) }
);

# only really needed for multibyte characters, not considered here (relying on
# perl's default IO layers to handle unicode and give character semantics)
has width => (is => 'rw', isa => "Int", default => 1);

use constant {
    alpha       => qr/[a-z]/,
    number      => qr/[0-9]/,
    operator    => qr/[<=]/,
    space       => qr/\s/,
};

sub add_input($self, $input) {
    my $cur = $self->input // "";
    # reset for new input, saving the total chars consumed for item emissions
    $self->total($self->total + $self->pos);
    $self->pos(0);
    $self->input($input);
}

sub next_state ($self) {
    my $next = $self->next;
    if ($next eq '') {
        return "done";
    }

    $self->backup;
    return "id" if $next =~ alpha;
    return "number" if $next =~ number;
    return "operator" if $next =~ operator;
    return "space" if $next =~ space;
    return "unrecognized";
}

my %states = (
    number => sub ($l) {
        while ($l->peek =~ number) {
            $l->next;
        }

        $l->emit("number");
        return "space";
    },

    id => sub ($l) {
        while ($l->peek =~ alpha) {
            $l->next;
        }

        my $cur = $l->current;

        if (my $key = $l->is_keyword($cur)) {
            $l->emit($key);
        } else {
            $l->emit("id");
        }

        return "space";
    },

    operator => sub ($l) {
        while ($l->peek =~ operator) {
            $l->next;
        }

        my $cur = $l->current;
        if (my $op = $l->is_operator($cur)) {
            $l->emit($op);
        } else {
            $l->emit("unrecognized");
        }
        return "space";
    },

    space => sub ($l) {
        while ($l->peek =~ space) {
            $l->next;
        }

        $l->skip; # or if you want spaces as tokens: $l->emit("space");
        return $l->next_state;
    },
);

sub is_keyword ($self, $word) {
    state $keys = {
        if => "IF",
        then => "THEN",
        end => "END",
    };

    return $keys->{$word};
}

sub is_operator ($self, $op) {
    state $operators = {
        '=' => 'assign',
        '==' => 'eq',
        '>' => 'gt',
        '<' => 'lt',
        '>=' => 'gte',
        '<=' => 'lte',
    };

    return $operators->{$op};
}

sub next ($self) {
    if ($self->pos >= length $self->input) {
        $self->width(0);
    }

    my $char = substr $self->input, $self->pos, $self->width;

    $self->pos($self->pos + $self->width);
    return $char;
}

sub backup ($self) {
    $self->pos($self->pos - $self->width);
}

sub peek ($self) {
    my $c = $self->next;
    $self->backup;
    return $c;
}

sub current ($self) {
    my $len = $self->pos - $self->start;
    my $value = substr $self->input, $self->start, $len;
    return $value;
}

sub emit ($self, $type) {
    my $value = $self->current;
    my $item = {type => $type, pos => $self->total + $self->start, val => $value};
    if ($type eq "error") {
        my $len = $self->pos - $self->start;
        my $actual = $self->next_state;
        my $expected = $self->state;
        if ($actual ne "unrecognized") {
            $item->{val} = sprintf "error at position %s! expected a '%s' but actually we found a '%s'", $self->pos, $expected, $actual;
        } else {
            $item->{val} = sprintf "unrecognized character '%s' at position %s", $self->peek, $self->pos;
        }
    }

    $self->emit_cb->($item);
    $self->start($self->pos);
}

sub skip ($self) {
    $self->start($self->pos);
}

sub run ($self) {
    $self->state($self->next_state);
    $self->width(1);
    while ($self->state ne "done") {
        my $pos = $self->pos;
        my $next = $states{$self->state}->($self);
        my $new_pos = $self->pos;

        # failed to advance the lexer, so the expected state didn't absorb any characters
        if ($next eq "unrecognized" || $pos == $new_pos) {
            $self->emit("error") and last;
        }

        $self->state($next);
    }
}

__PACKAGE__->meta->make_immutable;
1;
