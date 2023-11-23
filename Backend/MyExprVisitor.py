from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from Restaurant import Restaurant


class MyExprVisitor(ExprVisitor):
    def __init__(self, restaurant):
        super(MyExprVisitor, self).__init__()
        self.restaurant = restaurant
        self.stack = []  # Stack to evaluate the expression

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        print("[MyExprVisitor] visitProg()")
        response = "Default parser response " + self.restaurant.balance

        if ctx.OP_SHOWBALANCE():
            response = self.restaurant.balance

        self.stack.append(response)
        print("[MyExprVisitor] visitProg() --> FINISHED")
        return response
        # return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx: ExprParser.ExprContext):
        print("[MyExprVisitor] visitInfixExpr()")
        # self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        # Evaluate the right expression and push to stack
        # self.visit(ctx.right)

        # b = self.stack.pop()  # Why is ‘b’ the first popped item?
        # a = self.stack.pop()
        # c = None

        response = "Default parser response"

        if ctx.OP_SHOWBALANCE():
            response = self.restaurant.balance

        self.stack.append(response)
        print("[MyExprVisitor] visitInfixExpr() --> FINISHED")
        return response

    # Visit a parse tree produced by ExprParser#numberExpr.
    # def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
    #     c = int(str(ctx.INT()))  # Found a number, just insert to stack
    #     self.stack.append(c)
    #     return c

    # # Visit a parse tree produced by ExprParser#parensExpr.
    # def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
    #     # Since enclosed by parents, just visit expr
    #     return self.visit(ctx.expr())
