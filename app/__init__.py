from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Initialize database
    with app.app_context():
        from app.database import init_db
        init_db()

    # Register Blueprints
    from app.controllers.main import main_bp
    from app.controllers.product import product_bp  
    from app.controllers.auth import auth_bp  
    from app.controllers.cart import cart_bp  
    from app.controllers.wishlist import wishlist_bp  
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(wishlist_bp)
    return app
