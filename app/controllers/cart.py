from flask import jsonify, request
from flask_login import login_required, current_user
from app.models.cart   import Cart
from app.models.product import Product
from flask import Blueprint, render_template
from flask import request, redirect, url_for, flash
from app import db
# Initialize the Blueprint first
cart_bp = Blueprint('cart', __name__)
@cart_bp.route('/cart/add', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id')  # Get product_id from the form
    product = Product.query.get_or_404(product_id)

    # Check if the product is already in the cart
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = Cart(user_id=current_user.id, product_id=product_id)
        db.session.add(cart_item)

    db.session.commit()
    flash('Added to cart!', 'success')
    return redirect(url_for('main.home'))