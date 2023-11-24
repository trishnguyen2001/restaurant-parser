# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,81,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,13,
        1,13,1,14,4,14,74,8,14,11,14,12,14,75,1,15,1,15,1,15,1,15,0,0,16,
        1,0,3,0,5,0,7,0,9,0,11,0,13,0,15,0,17,0,19,0,21,0,23,1,25,2,27,3,
        29,4,31,5,1,0,12,2,0,83,83,115,115,2,0,72,72,104,104,2,0,79,79,111,
        111,2,0,87,87,119,119,2,0,66,66,98,98,2,0,65,65,97,97,2,0,76,76,
        108,108,2,0,78,78,110,110,2,0,67,67,99,99,2,0,69,69,101,101,2,0,
        10,10,13,13,3,0,9,10,13,13,32,32,70,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,
        37,1,0,0,0,7,39,1,0,0,0,9,41,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,
        15,47,1,0,0,0,17,49,1,0,0,0,19,51,1,0,0,0,21,53,1,0,0,0,23,55,1,
        0,0,0,25,68,1,0,0,0,27,70,1,0,0,0,29,73,1,0,0,0,31,77,1,0,0,0,33,
        34,7,0,0,0,34,2,1,0,0,0,35,36,7,1,0,0,36,4,1,0,0,0,37,38,7,2,0,0,
        38,6,1,0,0,0,39,40,7,3,0,0,40,8,1,0,0,0,41,42,5,95,0,0,42,10,1,0,
        0,0,43,44,7,4,0,0,44,12,1,0,0,0,45,46,7,5,0,0,46,14,1,0,0,0,47,48,
        7,6,0,0,48,16,1,0,0,0,49,50,7,7,0,0,50,18,1,0,0,0,51,52,7,8,0,0,
        52,20,1,0,0,0,53,54,7,9,0,0,54,22,1,0,0,0,55,56,3,1,0,0,56,57,3,
        3,1,0,57,58,3,5,2,0,58,59,3,7,3,0,59,60,3,9,4,0,60,61,3,11,5,0,61,
        62,3,13,6,0,62,63,3,15,7,0,63,64,3,13,6,0,64,65,3,17,8,0,65,66,3,
        19,9,0,66,67,3,21,10,0,67,24,1,0,0,0,68,69,5,40,0,0,69,26,1,0,0,
        0,70,71,5,41,0,0,71,28,1,0,0,0,72,74,7,10,0,0,73,72,1,0,0,0,74,75,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,30,1,0,0,0,77,78,7,11,0,0,
        78,79,1,0,0,0,79,80,6,15,0,0,80,32,1,0,0,0,2,0,75,1,0,1,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OP_SHOWBALANCE = 1
    OPEN_PAREN = 2
    CLOSE_PAREN = 3
    NEWLINE = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "OP_SHOWBALANCE", "OPEN_PAREN", "CLOSE_PAREN", "NEWLINE", "WS" ]

    ruleNames = [ "S", "H", "O", "W", "UNDERSCORE", "B", "A", "L", "N", 
                  "C", "E", "OP_SHOWBALANCE", "OPEN_PAREN", "CLOSE_PAREN", 
                  "NEWLINE", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


