from app import db

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(100), db.ForeignKey('product.name'), nullable=False)  # Add this line
    quantity = db.Column(db.Integer, default=1)

    # Relationship with Product
    product = db.relationship('Product', backref='carts')