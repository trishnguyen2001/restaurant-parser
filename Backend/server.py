from flask import Flask, abort, make_response, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


def handleUserInput(prompt):
    if (prompt == "cat"):
        return "=^owo^="
    return ("User prompt parsed: " + prompt)


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
    app.run()
