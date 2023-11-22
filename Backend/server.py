from flask import Flask, abort, make_response, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from datetime import datetime
import time

from antlr4 import *
from Restaurant import Restaurant
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

app = Flask(__name__)
CORS(app)


def handleUserInput(prompt):
    print("user prompt = " + prompt)
    if (prompt == "testing"):
        return "It works!"

    lexer = ExprLexer(prompt)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    print("tree starting")
    response = MyExprVisitor(r).visitInfixExpr(tree)
    time.sleep(5)

    return response.__str__


@app.route('/', methods=['GET', 'POST'])
def user_input():
    data = request.get_json()
    try:
        # parse user prompt
        print("Flask server request received")
        response = handleUserInput(data['userPrompt'])
        return jsonify(response)
    except Exception as e:
        abort(make_response(jsonify({
            'error': 'An error occurred',
            'message': str(e)}), 500)
        )


if __name__ == '__main__':
    app.debug = True
    r = Restaurant()
    app.run()
