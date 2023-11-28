from flask import Flask, abort, make_response, request, jsonify, session, copy_current_request_context
from flask_cors import CORS
from flask_session import Session
import time
import traceback

from antlr4 import *
from Restaurant import Restaurant
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

app = Flask(__name__)
CORS(app)
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = "password"
app.config["SESSION_TYPE"] = "filesystem"
        
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
        app.restaurant = r # updates app's restaurant instance

@app.route('/', methods=['GET', 'POST'])
def user_input():
    data = request.get_json()
    try:
        print("Flask server request received")

        handleUserInput(app.restaurant, data['userPrompt'])
        if (session.get("parsedResponse") == None):
            session['parsedResponse'] = "No response"
        print("parsedResponse = ", session.get("parsedResponse"))


    except Exception as e:
        session['parsedResponse'] = "ERROR: " + str(e) 
        traceback.print_exc()

    # sends response back to React server
    return(jsonify(session.get("parsedResponse")))

if __name__ == '__main__':
    app.debug = True
    app.restaurant = Restaurant()
    app.run()
