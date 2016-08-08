use strict;
use warnings;
use 5.22.0;
use utf8;
use lib 'lib';
use experimental qw(signatures postderef);

use Data::Dumper qw(Dumper);
$Data::Dumper::Sortkeys = 1;

use Lexer;

my @lexemes;
my $lex = Lexer->new(
    emit_cb => sub ($lexeme) {
        push @lexemes, $lexeme;
    }
);

# woooo stream it
while (my $line = <>) {
    $lex->add_input($line);
    $lex->run()
}

say Dumper(\@lexemes);
