from . import db

class MealsInOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)