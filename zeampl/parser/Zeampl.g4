grammar Zeampl;

module: decl* ;

decl: var_decl | func_decl | type_decl | class_decl;

var_decl: 'var' ID type_expr ('=' expr)? ';' ;
func_decl: ('func' ID | 'init') '(' arg_list? ')' type_expr? block;
arg_list: arg (',' arg)*;
arg: 'ID' type_expr;
type_decl: 'type_expr' ID '=' type_expr ';' ;
class_decl: 'class' ID '{' decl* '}';

type_expr: 'int' | 'bool' | list_type | tuple_type;
list_type: '[' type_expr ']';
tuple_type: '(' (type_expr ',' (type_expr (',' type_expr)* )? )? ')';


statement: block | expr_stmt | if_stmt | while_stmt | for_stmt | return_stmt | break_stmt | continue_stmt;
block: '{' statement* '}';
expr_stmt: expr (assign_op expr)? ';';
assign_op: '='| '+='| '-='| '~='| '*='| '/='| '%='| '&='| '|='| '^='| '<<='| '>>=';
if_stmt: 'if' expr block ('elif' expr block)* ('else' block)? ;
while_stmt: 'while' expr block ;
for_stmt: 'for' ID 'in' expr block ;
return_stmt: 'return' expr? ';' ;
break_stmt: 'break' ';' ;
continue_stmt: 'continue' ';' ;

expr: expr5;
expr5: expr4 (expr5op expr4)*;
expr5op: '==' | '!=' | '<' | '>' | '>=' | '<=' ;
expr4: expr3 (expr4op expr3)* ;
expr4op: '+' | '-' | '|' | '^' ;
expr3: expr2 (expr3op expr2)* ;
expr3op: '*' | '/' | '%' | '&' | '<<' | '>>' ;
expr2: (expr2op expr2) | expr1;
expr2op: '+' | '-' | '!' ;

expr1
  : expr0
    ( '.' ID
    | '(' expr (',' expr)* ')'
    )*
  ;

expr0: ID | literal | '(' expr ')' ;
literal: INT | BOOL | STRING | tuple_literal | list_literal;

tuple_literal: '(' (expr ',' (expr (',' expr)* )? )? ')' ;
list_literal: '[' (expr (',' expr)* )? ']' ;

ID: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;
INT: ('0'..'9')+;
BOOL: 'true' | 'false';
STRING: UNTERMINATED_STRING '"';
UNTERMINATED_STRING: '"' (~["\\\r\n] | '\\' (. | EOF))* ;
