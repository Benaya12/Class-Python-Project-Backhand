from models.admin import Admin
from models.foodType import FoodType
from models.meal import Meal
from models.order import Order
from models.mealsInOrder import MealsInOrder
from models.table import Table
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dani2802@localhost/restaurant'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()