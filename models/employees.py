from . import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)