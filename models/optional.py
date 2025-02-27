from . import db

class Optional(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    option = db.Column(db.String(50), nullable=False)
    