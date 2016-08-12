use v6;
#use lib 'lib';
#use Golang::Grammar;

my @tests = (
    import-decl => (
        'import plink "net/http"',
        'import "net"',
        'import "net/http"',
        'import _ "net/http"',
        'import (
            "foo";
            "bar";
            "blorg/pop";
        )',
        'import (
            "foo";
            bar "qux";
            _ "bloop";
        )',
    ),

    func-type => (
        'func(int, int, float64) (float64, *[]int)',
        'func(n int) func(p *[]int)',
        'func()',
        'func(x, y, z int) int',
        'func(x int, y int, z int) int',
        'func(a, _ int, z float32) bool',
        'func(a, b int, z float32) (bool)',
        'func(prefix string, values ...int)',
        'func(a, b int, z float64, opt ...interface{}) (success bool)'
    ),
    package-clause => (
        'package main',
        'package blorgbar'
    ),
    qualified-ident => (
        'net.http',
        'net.port',
    ),
);

#TODO: expressions?????

grammar Golang::Grammar {
    token TOP { <package-clause> ";"[<import-decl> ";"]+ [<top-level-decl> ";"]+ }

    # TODO: package name can't be blank identifier
    rule package-clause {
        "package" <package-name>
    }

    token package-name {
        <identifier>
    }

    token qualified-ident {
        <package-name>"."<identifier>
    }

    token import-decl {
        "import"<.ws>?[ <import-spec> | "("<.ws>?[<import-spec> ";"<.ws>?]* ")" ]
    }

    token import-spec {
        [ "." | <package-name>]?<.ws><import-path=.string-lit>
    }

    token top-level-decl {
        [
        | <declaration>
        #| <func-decl>
        #| <method-decl>
        ]
    }

    token declaration {
        [
        |<const-decl>
        |<type-decl>
        |<var-decl>
        ]
    }

    token const-decl {
        "const"<.ws>?[<const-spec>|"(" [ <const-spec> ";" ]+ ")" ]
    }

    token const-spec {
        <identifier-list> [ <type>?<.ws>"="<.ws><expression-list> ]?
    }

    token var-decl {
        "var"<.ws> [ <var-spec> | "(" [ <var-spec> ";" ]+ ")" ]
    }

    token var-spec {
        <identifier-list> [ <type> [ [ "="<.ws>?<expression-list> ]? | "="<.ws>?<expression-list>] ]
    }

    token expression-list {
        <expression> [","<.ws>?<expression>]*
    }

    token expression {
        [
        |<unary-expr>
        |<expression><.ws><binary-op><expression>
        ]
    }

    token binary-op {
        [
        | "||"
        | "&&"
        | <rel-op>
        | <add-op>
        | <mul-op>
        ]
    }

    token rel-op {
        [
        | "=="
        | "!="
        | "<"
        | "<="
        | ">"
        | ">="
        ]
    }

    token add-op {
        [
        | "+"
        | "-"
        | "|"
        | "^"
        ]
    }

    token mul-op {
        [
        | "*"
        | "/"
        | "%"
        | "<<"
        | ">>"
        | "&"
        | "&^"
        ]
    }

    token unary-expr {
        [
        |<primary-expr>
        |<unary-op><.ws><unary-expr>
        ]
    }

    token unary-op {
        [
        | "+"
        | "-"
        | "!"
        | "^"
        | "*"
        | "&"
        | "<-"
        ]
    }

    token type-decl {
        "type"<.ws>[<type-spec>|"(" [<type-spec> ";"]+]
    }

    rule type-spec {
        <identifier> <type>
    }

    token string-lit {
        [
        | <raw-string-lit>
        | <interpreted-string-lit>
        ]
    }

    #regex for backtracking
    regex raw-string-lit {
        '`' ["\n" | .]+'`'
    }

    #ditto
    regex interpreted-string-lit { '"'.+'"'  }

    token func-type { "func" <signature> }

    rule signature { <parameters> <result>? }
    token result { <parameters> | <type> }
    token parameters {
        "(" [<parameter-list> ","?]? ")"
    }
    rule parameter-list {
        <parameter-dec>["," <parameter-dec>]*
    }

    # this needs to be a regex because types look like identifiers, and
    # tokens/rules can't backtrack
    regex parameter-dec {
        <identifier-list>?<.ws>?"..."?<.ws>?<type>
    }

    rule identifier-list {
        <identifier>["," <identifier>]*
    }

    token identifier {
        [_|<:L>]\w*
    }

    token type {
        [
        |<type-name>
        |<type-lit>
        |"(" <type> ")"
        ]
    }

    token type-name {
        [
        |<identifier>
        |<qualified-ident>
        ]
    }

    token type-lit {
        [
        | <array-type>
        #| <struct-type> #TODO
        | <pointer-type>
        | <func-type>
        #| <interface-type> #TOTEST
        | <slice-type>
        #| <map-type> #TODO
        #| <channel-type> #TODO
        | <numeric-type>
        | <boolean-type>
        |"string"
        |'interface{}'
        ]
    }

    # token interface-type { "interface{" [<method-spec> ";"]* "}" }

    token method-spec {
        <method-name=.identifier> [<signature> | <interface-type-name=.type-name>]
    }

    token array-type {
        # "["<array-length=.expression>"]"<element-type=.type> #TODO: expression
        "["$<array-length>=(\d+)"]"<element-type=.type>
    }

    # TODO!
    #rule struct-type { "struct" "{" }

    token slice-type {
        "[]"<element-type=.type>
    }

    token pointer-type {
        "*"<base-type=.type>
    }

    token boolean-type { 'bool' }

    token boolean {
        [
        | 'true'
        | 'false'
        ]
    }

    token special-numeric-type {
        [
        | 'uint'
        | 'int'
        | 'uintptr'
        ]
    }

    token numeric-type {
        [
        | <special-numeric-type>
        | 'uint8'       # the set of all unsigned  8-bit integers (0 to 255)
        | 'uint16'      # the set of all unsigned 16-bit integers (0 to 65535)
        | 'uint32'      # the set of all unsigned 32-bit integers (0 to 4294967295)
        | 'uint64'      # the set of all unsigned 64-bit integers (0 to 18446744073709551615)

        | 'int8'        # the set of all signed  8-bit integers (-128 to 127)
        | 'int16'       # the set of all signed 16-bit integers (-32768 to 32767)
        | 'int32'       # the set of all signed 32-bit integers (-2147483648 to 2147483647)
        | 'int64'       # the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

        | 'float32'     # the set of all IEEE-754 32-bit floating-point numbers
        | 'float64'     # the set of all IEEE-754 64-bit floating-point numbers

        | 'complex64'   # the set of all complex numbers with float32 real and imaginary parts
        | 'complex128'  # the set of all complex numbers with float64 real and imaginary parts

        | 'byte'        # alias for uint8
        | 'rune'        # alias for int32
        ]
    }
}

for @tests -> $test {
    my ($rule, $targets) = $test.kv;
    print "testing $rule";
    for $targets.list -> $target {
        my $res = Golang::Grammar.subparse($target, rule => $rule);
        die "blagh '$target' doesn't parse under $rule!" if !$res;
    }
    say "... success!";
}
