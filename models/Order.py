from config import db
""" from models import Customer
 """


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    createDate = db.Column(db.DateTime, nullable=False)
    customerId = db.Column(db.Integer, db.ForeignKey(
        'customer.id'), nullable=True)
    customer = db.relationship(
        'Customer', backref='order', foreign_keys=[customerId])
    payment = db.relationship('Payment', backref='order', uselist=False)
