from flask import Flask, request, jsonify 
from flask_cors import CORS 
import os

@app.route('/cashier', methods=['GET'])
def display_cashier():
    pass