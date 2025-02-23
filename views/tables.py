from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/test', methods=['POST'])
def addOrder():
    pass
@app.route('/test', methods=['GET'])
def getOrders():
    pass
@app.route('/test', methods=['DEL'])
def removeOrder():
    pass
@app.route('/test', methods=['put'])
def editOrder():
    pass



if __name__ == '__main__':
    app.run(debug=True)
