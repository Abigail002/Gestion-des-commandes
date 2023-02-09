from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_mode = db.Column(db.String(255), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': payment_mode
    }
    orderId = db.Column(db.Integer, db.ForeignKey(
        'order.id'), nullable=True)
    order = db.relationship(
        'order', backref='payment', foreign_keys=[orderId])
