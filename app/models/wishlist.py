from app import db
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(100), db.ForeignKey('product.name'), nullable=False)  # Use product_name
    # You can add more fields if needed, like a timestamp

    # Relationship with Product
    product = db.relationship('Product', backref='wishlists')