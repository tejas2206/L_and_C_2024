from extensions import db

class Order(db.Model):
    __tablename__ = 'oop_orders'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipping_method = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    discount = db.Column(db.Float, default=0.00)
    shipping_cost = db.Column(db.Float, nullable=False)
    sub_total = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
