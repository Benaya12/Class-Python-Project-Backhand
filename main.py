from models.admin import Admin
from models.foodType import FoodType
from models.meal import Meal
from models.mealsInOrder import MealsInOrder
from models.order import Order
from models.table import Table
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dani2802@localhost/restaurant'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
