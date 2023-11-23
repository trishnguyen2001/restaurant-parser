from flask import Flask, abort, make_response, request, jsonify, session, copy_current_request_context
from flask_cors import CORS
from flask_session import Session
import time

from antlr4 import *
from Restaurant import Restaurant
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

app = Flask(__name__)
CORS(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
        

@app.route('/', methods=['GET', 'POST'])
def user_input():

    @copy_current_request_context
    def handleUserInput(prompt):
        print("user prompt = " + prompt)
        if (prompt == "testing"):
            session['parsedResponse'] = "It works!"
        elif(prompt == "SHOW_BALANCE"):
            print("SHOW_BALANCE called!")
            lexer = ExprLexer(InputStream(prompt))
            stream = CommonTokenStream(lexer)
            parser = ExprParser(stream)
            print("parser.prog() starting...")
            tree = parser.prog()
            print("MyExprVisitor(r).visitProg(tree) starting...")
            parserRes = MyExprVisitor(session.get('r')).visitProg(tree)
            session['parsedResponse'] = parserRes
            print("Parsing finished! --> parserRes = ", parserRes)
            time.sleep(3)
    data = request.get_json()
    try:
        # parse user prompt
        print("Flask server request received")
        print("Restaurant = ", session.get('r'))
        handleUserInput(data['userPrompt'])
        if (session.get("parsedResponse") == None):
            session['parsedResponse'] = "No response"
        print("parsedResponse = ", session.get("parsedResponse"))
    except Exception as e:
        session['parsedResponse'] = "ERROR: " + str(e)
    return(jsonify(session.get("parsedResponse")))




if __name__ == '__main__':
    app.debug = True
    app.run()
    session['parsedResponse'] = None
    session['balance'] = 1000
