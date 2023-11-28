grammar Expr;
 
/* Parser Rules */
prog: prompt EOF;
prompt: command;
command: (
    OP_SHOWBALANCE | 
    OP_SHOWINVENTORY | 
    (OP_BUY '(' quantity=NUMBER ',' ingredient=INGREDIENT ')') |
    (OP_SELL '(' quantity=NUMBER ',' dish=DISHNAME ')') |
    (OP_NEWDISH '(' dishname=DISHNAME ',' cooking_method=COOKING_METHOD ',' temperature=NUMBER ',' cooking_time=NUMBER ')')
);

/* Lexer Rules */
fragment A: ('A' | 'a');
fragment B: ('B' | 'b');
fragment C: ('C' | 'c');
fragment D: ('D' | 'd');
fragment E: ('E' | 'e');
fragment F: ('F' | 'f');
fragment G: ('G' | 'g');
fragment H: ('H' | 'h');
fragment I: ('I' | 'i');
fragment J: ('J' | 'j');
fragment K: ('K' | 'k');
fragment L: ('L' | 'l');
fragment M: ('M' | 'm');
fragment N: ('N' | 'n');
fragment O: ('O' | 'o');
fragment P: ('P' | 'p');
fragment Q: ('Q' | 'q');
fragment R: ('R' | 'r');
fragment S: ('S' | 's');
fragment T: ('T' | 't');
fragment U: ('U' | 'u');
fragment V: ('V' | 'v');
fragment W: ('W' | 'w');
fragment X: ('X' | 'x');
fragment Y: ('Y' | 'y');
fragment Z: ('Z' | 'z');

fragment OPEN_BRACKET : '[';
fragment CLOSE_BRACKET : ']';
fragment UNDERSCORE: ('_');
fragment DIGIT : [0-9];
fragment SPACE: ' ';
fragment APOSTROPHE: '\'';

OP_SHOWBALANCE : S H O W UNDERSCORE B A L A N C E;
OP_SHOWINVENTORY : S H O W UNDERSCORE I N V E N T O R Y;
OP_BUY : B U Y;
OP_SELL : S E L L;
OP_NEWDISH : N E W UNDERSCORE D I S H;

NUMBER : (DIGIT)+;

INGREDIENT : (
    (B E E F) | 
    (P O T A T O) | 
    (R I C E) | 
    (C H I C K E N) | 
    (A S P A R A G U S) | 
    (L E T T U C E) |
    (T O M A T O) |
    (C U C U M B E R) |
    (B R O C C O L I) |
    (S A L M O N) |
    (P A S T A) |
    (S U G A R) |
    (F L O U R)
);
DISHNAME : (
    (T R I S H APOSTROPHE S SPACE C H I C K E N) |
    (S P A G H E T T I) |
    (R A V I O L I) |
    (T E E APOSTROPHE S SPACE S A L M O N) |
    (T N T SPACE B U R G E R) |
    (S K I N N Y SPACE S A L A D)
);
COOKING_METHOD : (
    (S E A R) |
    (B A K E) |
    (B O I L) |
    (N O N E)
);

NEWLINE : [\r\n]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);