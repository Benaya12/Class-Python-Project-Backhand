from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/test', methods=['GET'])
def get_books():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(debug=True)