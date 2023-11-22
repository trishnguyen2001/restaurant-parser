grammar Expr;
 
// prog: expr EOF;

// sub-rule w/ multiple alternatives
// expr: left=expr op=('+'|'-') right=expr   #infixExpr
    //| left=expr op=('*'|'/') right=expr   #infixExpr
    //| INT                                 #numberExpr
    //| '(' expr ')'                        #parensExpr
    //;
 

// rules
OP_SHOWBALANCE: 'SHOW_BALANCE';
 
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);