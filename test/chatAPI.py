from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
#import socket

app = Flask(__name__)
CORS(app)

@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

@app.route('/users', methods=['GET'])
def get_users():
    result = users
    return jsonify({'users': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)