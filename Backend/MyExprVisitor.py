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
            response = "BALANCE = $" + '{0:.2f}'.format(self.restaurant.balance)
        elif ctx.OP_SHOWINVENTORY():
            print("[MyExprVisitor] visitCommand(): ctx.OP_SHOWINVENTORY")
            response = "INVENTORY = " + str(self.restaurant.get_inventory())
        elif ctx.OP_BUY():
            print("[MyExprVisitor] visitCommand(): ctx.OP_BUY")
            print("ingredient = ", ctx.ingredient.text)
            print("quantity = " , ctx.quantity.text)
            response = self.restaurant.buy(int(ctx.quantity.text), ctx.ingredient.text)
        elif ctx.OP_NEWDISH():
            print("[MyExprVisitor] visitCommand(): ctx.OP_NEWDISH")
            #print("dish name = ", ctx.dishname.text)
            #print("price = " , ctx.price.text)
            #print("cooking method = " , ctx.cooking_method.text)
            #print("temp = " , ctx.temperature.text)
            #print("cooking time = " , ctx.cooking_duration.text)
            response = self.restaurant.new_dish(int(ctx.price.text), int(ctx.temperature.text))

        self.stack.append(response)
        print("[MyExprVisitor] visitCommand() --> FINISHED")
