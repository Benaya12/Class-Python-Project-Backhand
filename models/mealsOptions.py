from . import db

class MealsOptions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('MealsInOrder.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('Optional.id'), nullable=False)

