grammar Zeampl;

module: decl* ;

decl: varDecl | funcDecl | typeDecl | classDecl;

varDecl: 'var' ID type_expr ('=' expr)? ';' ;
funcDecl: ('func' ID | 'init') '(' argList? ')' type_expr? block;
argList: arg (',' arg)*;
arg: 'ID' type_expr;
typeDecl: 'type_expr' ID '=' type_expr ';' ;
classDecl: 'class' ID '{' decl* '}';

type_expr: 'int' | 'bool' | list_type | tuple_type;
list_type: '[' type_expr ']';
tuple_type: '(' (type_expr ',' (type_expr (',' type_expr)* )? )? ')';


statement: block | exprStmt | ifStmt | whileStmt | forStmt | returnStmt | breakStmt | continueStmt;
block: '{' statement* '}';
exprStmt: expr (assign_op expr)? ';';
assign_op: '='| '+='| '-='| '~='| '*='| '/='| '%='| '&='| '|='| '^='| '<<='| '>>=';
ifStmt: 'if' expr block ('elif' expr block)* ('else' block)? ;
whileStmt: 'while' expr block ;
forStmt: 'for' ID 'in' expr block ;
returnStmt: 'return' expr? ';' ;
breakStmt: 'break' ';' ;
continueStmt: 'continue' ';' ;

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
literal: intLiteral | boolLiteral | stringLiteral | tupleLiteral | listLiteral;
intLiteral: INT;
boolLiteral: BOOL;
stringLiteral: STRING;
tupleLiteral: '(' (x+=expr ',' (x+=expr (',' x+=expr)* )? )? ')' ;
listLiteral: '[' (x+=expr (',' x+=expr)* )? ']' ;

BOOL: 'true' | 'false';
ID: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;
INT: ('0'..'9')+;
STRING: UNTERMINATED_STRING '"';
fragment UNTERMINATED_STRING: '"' (~["\\\r\n] | '\\' ESCAPE)* ;
fragment ESCAPE
  : '\\' | '\'' | '\"'
  | 'a' | 'b' | 'f' | 'n' | 'r' | 't' | 'v'
  | 'x' HEX_DIGIT HEX_DIGIT
  | 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
  | 'U' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
  ;
fragment HEX_DIGIT: '0'..'9' | 'a'..'f' | 'A'..'F' ;

WS: (' ' | '\t' | '\n')+ -> skip;
