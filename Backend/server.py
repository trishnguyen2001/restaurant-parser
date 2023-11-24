from flask import Flask, abort, make_response, request, jsonify, session, copy_current_request_context
from flask_cors import CORS
from flask_session import Session
import time
import traceback

from antlr4 import *
from Restaurant import Restaurant
from RestaurantSession import RestaurantSession, RestaurantSessionInterface
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

app = Flask(__name__)
CORS(app)
Session(app)
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = "password"
app.config["SESSION_TYPE"] = "filesystem"
app.session_cookie_name = "sessioncookie"
app.session_interface = RestaurantSessionInterface()
global sessionInterface
        

@app.route('/', methods=['GET', 'POST'])
def user_input():

    # executes MyExprVisitor for parsing
    def handleUserInput(r, prompt):
        print("prompt: " + prompt)
        if (prompt == "testing"):
            session['parsedResponse'] = "It works!"
        else:
            lexer = ExprLexer(InputStream(prompt))
            stream = CommonTokenStream(lexer)
            parser = ExprParser(stream)
            print("Parsing starting...")
            tree = parser.prog()
            session['parsedResponse'] = MyExprVisitor(r).visitProg(tree)
            print("Parsing finished!")
            time.sleep(3)

    data = request.get_json()
    try:
        print("Flask server request received")

        # opens session
        sessionInterface = RestaurantSessionInterface(Restaurant())
        rSession = sessionInterface.open_session(app, request)
        print("Active Session: \nbalance = ", rSession.restaurant.balance, 
                    "\n ingrList = ", rSession.restaurant.ingredient_inventory, 
                    "\n dishList = ", rSession.restaurant.dish_inventory)
        rSession['parsedResponse'] = None

        # run parser based on user's input
        handleUserInput(rSession.restaurant, data['userPrompt'])
        # validates response from parser
        if (session.get("parsedResponse") == None):
            session['parsedResponse'] = "No response"
        print("parsedResponse = ", session.get("parsedResponse"))

        # saves session with current restaurant data
        sessionInterface.save_session(app, rSession, make_response())

    except Exception as e:
        session['parsedResponse'] = "ERROR: " + str(e) 
        traceback.print_exc()

    # sends response back to React server
    return(jsonify(session.get("parsedResponse")))




if __name__ == '__main__':
    app.debug = True
    app.run()
