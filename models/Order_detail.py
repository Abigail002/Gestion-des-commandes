from config import db
""" from models import Order, Item
 """

class Order_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    taxStatus = db.Column(db.String(255), nullable=False)
    orderId = db.Column(db.Integer, db.ForeignKey(
        'order.id'), nullable=True)
    orderDetail = db.relationship(
        'Order', backref='order_detail', foreign_keys=[orderId])
    itemId = db.Column(db.Integer, db.ForeignKey(
        'item.id'), nullable=True)
    item = db.relationship(
        'Item', backref='order', foreign_keys=[itemId])
