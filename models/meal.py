from . import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    foodType = db.Column(db.Integer, db.ForeignKey('food_type.id'), nullable=False)