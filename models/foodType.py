from . import db

class FoodType(db.Model):
    __tablename__ = 'food_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)