from . import db

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    