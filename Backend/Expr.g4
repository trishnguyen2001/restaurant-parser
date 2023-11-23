grammar Expr;
 
prog: expr EOF;

expr: OP_SHOWBALANCE
;
 

/* rules */
OP_SHOWBALANCE: 'SHOW_BALANCE';
NEWLINE : [\r\n]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);