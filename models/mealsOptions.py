from . import db

class MealsOptions(db.Model):
    __tablename__ = 'meals_options'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals_in_order.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('optional.id'), nullable=False)

