from app import db
from app.models.product import Product  # Import your Product model
from app.models.user import User  # Import your User model
from app.models.cart import Cart  # Import your Cart model
from app.models.wishlist import Wishlist  # Import your Wishlist model
from werkzeug.security import generate_password_hash  # For hashing passwords

def init_db():
    db.create_all()

    # Sample products
    products = [
        Product(name="DARK FLORISH ONEPIECE", price=95.0, image="product-item-1.jpg", category="men"),
        Product(name="Elegant Dress", price=120.0, image="product-item-2.jpg", category="women"),
    ]

    # Check if the user already exists
    user = User.query.filter_by(email="admin@example.com").first()
    if not user:
        # Create a new user if it doesn't exist
        user = User(
            username="admin",
            email="admin@example.com",
        )
        user.set_password("password123")  # Hash the password
        db.session.add(user)

    # Add products to the session
    db.session.bulk_save_objects(products)

    # Commit changes to the database
    db.session.commit()