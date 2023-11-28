# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,38,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,2,0,0,3,0,2,4,0,0,38,0,6,1,0,
        0,0,2,9,1,0,0,0,4,35,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,
        9,10,3,4,2,0,10,3,1,0,0,0,11,36,5,4,0,0,12,36,5,5,0,0,13,14,5,6,
        0,0,14,15,5,1,0,0,15,16,5,9,0,0,16,17,5,2,0,0,17,18,5,10,0,0,18,
        36,5,3,0,0,19,20,5,7,0,0,20,21,5,1,0,0,21,22,5,9,0,0,22,23,5,2,0,
        0,23,24,5,11,0,0,24,36,5,3,0,0,25,26,5,8,0,0,26,27,5,1,0,0,27,28,
        5,11,0,0,28,29,5,2,0,0,29,30,5,12,0,0,30,31,5,2,0,0,31,32,5,9,0,
        0,32,33,5,2,0,0,33,34,5,9,0,0,34,36,5,3,0,0,35,11,1,0,0,0,35,12,
        1,0,0,0,35,13,1,0,0,0,35,19,1,0,0,0,35,25,1,0,0,0,36,5,1,0,0,0,1,
        35
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "OP_SHOWBALANCE", "OP_SHOWINVENTORY", "OP_BUY", "OP_SELL", 
                      "OP_NEWDISH", "NUMBER", "INGREDIENT", "DISHNAME", 
                      "COOKING_METHOD", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_prompt = 1
    RULE_command = 2

    ruleNames =  [ "prog", "prompt", "command" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    OP_SHOWBALANCE=4
    OP_SHOWINVENTORY=5
    OP_BUY=6
    OP_SELL=7
    OP_NEWDISH=8
    NUMBER=9
    INGREDIENT=10
    DISHNAME=11
    COOKING_METHOD=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prompt(self):
            return self.getTypedRuleContext(ExprParser.PromptContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.prompt()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PromptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ExprParser.CommandContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_prompt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrompt" ):
                listener.enterPrompt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrompt" ):
                listener.exitPrompt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrompt" ):
                return visitor.visitPrompt(self)
            else:
                return visitor.visitChildren(self)




    def prompt(self):

        localctx = ExprParser.PromptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prompt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.command()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.quantity = None # Token
            self.ingredient = None # Token
            self.dish = None # Token
            self.dishname = None # Token
            self.cooking_method = None # Token
            self.temperature = None # Token
            self.cooking_time = None # Token

        def OP_SHOWBALANCE(self):
            return self.getToken(ExprParser.OP_SHOWBALANCE, 0)

        def OP_SHOWINVENTORY(self):
            return self.getToken(ExprParser.OP_SHOWINVENTORY, 0)

        def OP_BUY(self):
            return self.getToken(ExprParser.OP_BUY, 0)

        def OP_SELL(self):
            return self.getToken(ExprParser.OP_SELL, 0)

        def OP_NEWDISH(self):
            return self.getToken(ExprParser.OP_NEWDISH, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NUMBER)
            else:
                return self.getToken(ExprParser.NUMBER, i)

        def INGREDIENT(self):
            return self.getToken(ExprParser.INGREDIENT, 0)

        def DISHNAME(self):
            return self.getToken(ExprParser.DISHNAME, 0)

        def COOKING_METHOD(self):
            return self.getToken(ExprParser.COOKING_METHOD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 11
                self.match(ExprParser.OP_SHOWBALANCE)
                pass
            elif token in [5]:
                self.state = 12
                self.match(ExprParser.OP_SHOWINVENTORY)
                pass
            elif token in [6]:
                self.state = 13
                self.match(ExprParser.OP_BUY)
                self.state = 14
                self.match(ExprParser.T__0)
                self.state = 15
                localctx.quantity = self.match(ExprParser.NUMBER)
                self.state = 16
                self.match(ExprParser.T__1)
                self.state = 17
                localctx.ingredient = self.match(ExprParser.INGREDIENT)
                self.state = 18
                self.match(ExprParser.T__2)
                pass
            elif token in [7]:
                self.state = 19
                self.match(ExprParser.OP_SELL)
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                localctx.quantity = self.match(ExprParser.NUMBER)
                self.state = 22
                self.match(ExprParser.T__1)
                self.state = 23
                localctx.dish = self.match(ExprParser.DISHNAME)
                self.state = 24
                self.match(ExprParser.T__2)
                pass
            elif token in [8]:
                self.state = 25
                self.match(ExprParser.OP_NEWDISH)
                self.state = 26
                self.match(ExprParser.T__0)
                self.state = 27
                localctx.dishname = self.match(ExprParser.DISHNAME)
                self.state = 28
                self.match(ExprParser.T__1)
                self.state = 29
                localctx.cooking_method = self.match(ExprParser.COOKING_METHOD)
                self.state = 30
                self.match(ExprParser.T__1)
                self.state = 31
                localctx.temperature = self.match(ExprParser.NUMBER)
                self.state = 32
                self.match(ExprParser.T__1)
                self.state = 33
                localctx.cooking_time = self.match(ExprParser.NUMBER)
                self.state = 34
                self.match(ExprParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





