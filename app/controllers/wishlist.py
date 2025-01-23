from flask import jsonify, request
from flask_login import login_required, current_user
from app.models.wishlist import Wishlist
from app.models.product import Product
from flask import request, redirect, url_for, flash
from app import db
from flask import Blueprint, render_template
# Initialize the Blueprint first
wishlist_bp = Blueprint('wishlist', __name__)
@wishlist_bp.route('/wishlist/add', methods=['POST'])
@login_required
def add_to_wishlist():
    product_id = request.form.get('product_id')  # Get product_id from the form
    product = Product.query.get_or_404(product_id)

    # Check if the product is already in the wishlist
    if not Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first():
        wishlist_item = Wishlist(user_id=current_user.id, product_id=product_id)
        db.session.add(wishlist_item)
        db.session.commit()
        flash('Added to wishlist!', 'success')
    else:
        flash('Product is already in your wishlist.', 'info')

    return redirect(url_for('main.home'))