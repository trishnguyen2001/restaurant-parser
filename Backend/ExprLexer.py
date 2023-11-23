# Generated from backend/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,22,8,1,11,1,12,1,23,1,2,1,2,1,
        2,1,2,0,0,3,1,1,3,2,5,3,1,0,2,2,0,10,10,13,13,3,0,9,10,13,13,32,
        32,29,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,0,3,21,1,0,0,
        0,5,25,1,0,0,0,7,8,5,83,0,0,8,9,5,72,0,0,9,10,5,79,0,0,10,11,5,87,
        0,0,11,12,5,95,0,0,12,13,5,66,0,0,13,14,5,65,0,0,14,15,5,76,0,0,
        15,16,5,65,0,0,16,17,5,78,0,0,17,18,5,67,0,0,18,19,5,69,0,0,19,2,
        1,0,0,0,20,22,7,0,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,4,1,0,0,0,25,26,7,1,0,0,26,27,1,0,0,0,27,28,6,2,
        0,0,28,6,1,0,0,0,2,0,23,1,0,1,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OP_SHOWBALANCE = 1
    NEWLINE = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'SHOW_BALANCE'" ]

    symbolicNames = [ "<INVALID>",
            "OP_SHOWBALANCE", "NEWLINE", "WS" ]

    ruleNames = [ "OP_SHOWBALANCE", "NEWLINE", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


