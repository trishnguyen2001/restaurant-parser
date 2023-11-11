from flask import Flask, abort, make_response, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

def parse(prompt):
    # do something here to get output
    response = pyrebase_auth.sign_in_with_email_and_password(email, password)
    return response

@app.route('/', methods=['POST'])
def user_input():
    data = request.get_json()
    try:
        # parse user prompt
        response = parse(data['prompt'])
        return jsonify(response)
    except Exception as e:
        abort(make_response(jsonify({
            'error': 'An error occurred',
            'message': str(e)}), 500)
        )

if __name__ == '__main__':
    app.debug = True
    app.run()
