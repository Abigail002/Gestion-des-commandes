from config import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    deliveryAddress = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean)
