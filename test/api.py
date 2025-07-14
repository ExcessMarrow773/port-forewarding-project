from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
#import socket

app = Flask(__name__)
CORS(app)

users = [{'name': "Atticus", 'id': 1}]


@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})


@app.route('/users', methods=['GET'])
def get_users():
    result = users
    return jsonify({'users': result})

@app.route('/post', methods=['POST'])
def post_test():
    if request.is_json:
        data = request.json

        response_message = f"Received JSON data: {data}"
        print(response_message)
        return jsonify({"message": response_message}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.route('/postUser', methods=['POST'])
def post_user():
    if request.is_json:
        data = request.json

        response_message = f"Received JSON data: {data}"
        data['id'] = len(users)+1
        users.append(data)
        print(response_message)
        return jsonify({"message": response_message}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)