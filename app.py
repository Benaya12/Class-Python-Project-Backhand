from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
import os
<<<<<<< Updated upstream
from config import Config
from models.admin import Admin
from models.foodType import FoodType
from models.meal import Meal
from models.mealsInOrder import MealsInOrder
from models.order import Order
from models.table import Table

=======
from models.user import db, User
from config import Config
>>>>>>> Stashed changes


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)
<<<<<<< Updated upstream
db.init_app(app)
=======
>>>>>>> Stashed changes

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/test', methods=['GET'])
def get_books():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)