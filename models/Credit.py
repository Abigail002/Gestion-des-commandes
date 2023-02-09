from config import db
from models.Payment import Payment

class Credit(Payment):
    id = db.Column(db.Integer, db.ForeignKey('payment.id'), primary_key=True)
    number = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    expireDate = db.Column(db.Date)
    __mapper_args__ = {
        'polymorphic_identity': 'credit',
    }
