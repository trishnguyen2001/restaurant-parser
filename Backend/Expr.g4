grammar Expr;
 
/* Parser Rules */
prog: prompt EOF;
prompt: command;
command: OP_SHOWBALANCE;
/* command: OP_SHOWBALANCE | OP_SHOWINVENTORY */
/* param: OPEN_PAREN INGREDIENT+ CLOSE_PAREN */

/* Lexer Rules */
fragment S: ('S' | 's');
fragment H: ('H' | 'h');
fragment O: ('O' | 'o');
fragment W: ('W' | 'w');
fragment UNDERSCORE: ('_');
fragment B: ('B' | 'b');
fragment A: ('A' | 'a');
fragment L: ('L' | 'l');
fragment N: ('N' | 'n');
fragment C: ('C' | 'c');
fragment E: ('E' | 'e');

OP_SHOWBALANCE: S H O W UNDERSCORE B A L A N C E;
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
NEWLINE : [\r\n]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);