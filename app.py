from flask import Flask, request, jsonify
from flask_cors import CORS

from config import Config

# Database models
from models import db
from models.admin import Admin
from models.foodType import FoodType
from models.meal import Meal
from models.mealsInOrder import MealsInOrder
from models.order import Order
from models.table import Table
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Views
from views.orders import Orders
from views.menu import Menu
from views.login import Login
from views.cashier import Cashier
from views.meals import Meals


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)
db.init_app(app)



with app.app_context():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    db.create_all()



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    Orders(app)
    Menu(app)
    Login(app)
    Cashier(app)
    Meals(app)

    app.run(debug=True)