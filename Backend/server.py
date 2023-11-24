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
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = "password"
# app.config["SESSION_COOKIE_NAME"] = "sessioncookie"
app.config["SESSION_TYPE"] = "filesystem"
app.session_cookie_name = "sessioncookie"
app.session_interface = RestaurantSessionInterface()
Session(app)
global sessionInterface
        

@app.route('/', methods=['GET', 'POST'])
def user_input():

    def handleUserInput(r, prompt):
        print("prompt: " + prompt)
        if (prompt == "testing"):
            session['parsedResponse'] = "It works!"
        else:
            lexer = ExprLexer(InputStream(prompt))
            stream = CommonTokenStream(lexer)
            parser = ExprParser(stream)
            print("parser.prog() starting...")
            tree = parser.prog()
            print("MyExprVisitor(r).visitProg(tree) starting...")
            print("Session retrieved\nbalance = ", r.balance, 
                    "\n ingrList = ", r.ingredient_inventory, 
                    "\n dishList = ", r.dish_inventory)
            parserRes = MyExprVisitor(r).visitProg(tree)
            session['parsedResponse'] = parserRes
            print("Parsing finished!")
            time.sleep(3)

    data = request.get_json()
    try:
        # parse user prompt
        print("Flask server request received")
        sessionInterface = RestaurantSessionInterface(Restaurant())
        rSession = sessionInterface.open_session(app, request)
        rSession['parsedResponse'] = None
        # print('restaurant = $', rSession.restaurant.balance)
        handleUserInput(rSession.restaurant, data['userPrompt'])
        if (session.get("parsedResponse") == None):
            session['parsedResponse'] = "No response"
        print("parsedResponse = ", session.get("parsedResponse"))
        sessionInterface.save_session(app, rSession, make_response())
    except Exception as e:
        session['parsedResponse'] = "ERROR: " + str(e) 
        traceback.print_exc()
    return(jsonify(session.get("parsedResponse")))




if __name__ == '__main__':
    app.debug = True
    app.run()
    # session['balance'] = 1000
