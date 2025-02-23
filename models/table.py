from . import db

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    max_capacity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    