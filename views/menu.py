from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/test', methods=['GET'])
def get_books():
    return jsonify({'message': 'Hello, World!'})

# Manage menu
@app.route('/test', methods=['POST'])
def addServing():
    pass

@app.route('/test', methods=['DELETE'])
def deleteServing():
    pass

@app.route('/test', methods=['GET, POST'])
def changeServing():
    pass

if __name__ == '__main__':
    app.run(debug=True)
