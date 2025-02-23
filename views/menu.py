from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Manage menu
@app.route('/test', methods=['POST'])
def addMeal():
    pass

@app.route('/test', methods=['DELETE'])
def deleteMeal():
    pass

@app.route('/test', methods=['GET, POST'])
def editMeal():
    pass

if __name__ == '__main__':
    app.run(debug=True)
