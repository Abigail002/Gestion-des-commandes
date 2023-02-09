from config import db
from models.Payment import Payment

class Wire_transfer(Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    bankId = db.Column(db.String(255), nullable=False)
    bankName = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'Wire_transfer',
    }