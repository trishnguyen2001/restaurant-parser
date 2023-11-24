from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from Restaurant import Restaurant


class MyExprVisitor(ExprVisitor):
    def __init__(self, restaurant):
        super(MyExprVisitor, self).__init__()
        self.restaurant = restaurant
        self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by ExprParser#prog
    def visitProg(self, ctx: ExprParser.ProgContext):
        print("[MyExprVisitor] visitProg()")
        return self.visit(ctx.prompt())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#prompt
    def visitPrompt(self, ctx: ExprParser.PromptContext):
        print("[MyExprVisitor] visitPrompt()")
        self.visit(ctx.command())
        response = self.stack.pop()
        return response

    # Visit a parse tree produced by ExprParser#command
    def visitCommand(self, ctx: ExprParser.CommandContext):
        print("[MyExprVisitor] visitCommand()")
        response = "Default parser response"
        if ctx.OP_SHOWBALANCE():
            print("[MyExprVisitor] visitCommand(): ctx.OP_SHOWBALANCE")
            response = "$" + '{0:.2f}'.format(self.restaurant.balance)
        self.stack.append(response)
        print("[MyExprVisitor] visitCommand() --> FINISHED")
        return response
