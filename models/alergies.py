from . import db

class Alergies(db.Model):
    __tablename__ = 'alergies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)



