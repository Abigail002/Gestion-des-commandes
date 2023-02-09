from config import db
from models.Payment import Payment

class Check(Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    bankId = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'check',
    }