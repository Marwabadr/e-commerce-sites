from flask import Blueprint, render_template
from app.models.product import Product
from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from flask import request, redirect, url_for, flash
from app import db
from app.models.cart   import Cart
from app.models.wishlist import Wishlist
# Initialize the Blueprint first
main_bp = Blueprint('main', __name__)
@main_bp.route('/')
def home():
    images = [
        "banner-image-1.jpg",
        "banner-image-2.jpg",
        "banner-image-3.jpg",
        "banner-image-4.jpg",
        "banner-image-5.jpg",
        "banner-image-6.jpg",
    ]
    products = [
        {"id":1,"name": "DARK FLORISH ONEPIECE", "price": 95.00, "image": "images/product-item-1.jpg","category":"men"}, 
        {"id":2,"name": "BAGGY SHIRT", "price": 55.00, "image": "images/product-item-2.jpg","category":"women"},
        {"id":3,"name": "COTTON OFF-WHITE SHIRT", "price": 65.00, "image": "images/product-item-3.jpg","category":"women"},
        {"id":4,"name": "CROP SWEATER", "price": 50.00, "image": "images/product-item-4.jpg","category":"men"},
    ]
    categories = [
        {"name": "SHOP FOR MEN", "image": "cat-item1.jpg", "endpoint": "product.shop_men"},
        {"name": "SHOP FOR WOMEN", "image": "cat-item2.jpg", "endpoint": "product.shop_women"},
        {"name": "SHOP ACCESSORIES", "image": "cat-item3.jpg", "endpoint": "product.shop_accessories"},
    ]
    return render_template('index.html', images=images, products=products, categories=categories)
# About route
@main_bp.route('/about')
def about():
    return render_template('about.html')


from urllib.parse import unquote
@main_bp.route('/cart/add/<path:product_name>', methods=['POST'])
@login_required
def add_to_cart(product_name):
    decoded_product_name = unquote(product_name).strip()
    print(f"Decoded product name: {decoded_product_name}")  # Debugging
    
    # Find the product by name
    product = Product.query.filter_by(name=decoded_product_name).first()
    print(f"Product found: {product}")  # Debugging
    
    # Add the product to the cart using product_name
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_name=product.name).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_id=current_user.id, product_name=product.name)
        db.session.add(cart_item)

    db.session.commit()
    flash('Product added to cart!', 'success')
    return redirect(url_for('main.home'))
# Route to add a product to the wishlist
@main_bp.route('/wishlist/add/<path:product_name>', methods=['POST'])
@login_required
def add_to_wishlist(product_name):
    decoded_product_name = unquote(product_name).strip()
    print(f"Decoded product name: {decoded_product_name}")  # Debugging
    
    # Find the product by name
    product = Product.query.filter_by(name=decoded_product_name).first()
    print(f"Product found: {product}")  # Debugging
    
    # Check if the product is already in the wishlist
    wishlist_item = Wishlist.query.filter_by(user_id=current_user.id, product_name=product.name).first()
    if wishlist_item:
        flash('Product is already in your wishlist!', 'info')
    else:
        # Add the product to the wishlist
        wishlist_item = Wishlist(user_id=current_user.id, product_name=product.name)
        db.session.add(wishlist_item)
        db.session.commit()
        flash('Product added to wishlist!', 'success')

    return redirect(url_for('main.home'))
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import db
from app.models.wishlist import Wishlist


@main_bp.route('/wishlist')
@login_required
def view_wishlist():
    # Fetch the wishlist items for the current user
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlist.html', wishlist_items=wishlist_items)
@main_bp.route('/cart')
@login_required
def view_cart():
    # Fetch the wishlist items for the current user
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    return render_template('cart.html', cart_items=cart_items)