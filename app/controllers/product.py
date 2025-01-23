from flask import Blueprint, render_template
from app.models.product import Product

# Initialize the Blueprint
product_bp = Blueprint('product', __name__)

# Product Details Route
@product_bp.route('/product/<int:product_id>')
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product/details.html', product=product)

# All Products Route
@product_bp.route('/products')
def all_products():
    products = Product.query.all()
    return render_template('product/all_products.html', products=products)
@product_bp.route('/shop/men')
def shop_men():
    # Fetch men's products from the database
    products = Product.query.filter_by(category="men").all()
    return render_template('product/shop_men.html', products=products)

@product_bp.route('/shop/women')
def shop_women():
    # Fetch women's products from the database
    products = Product.query.filter_by(category="women").all()
    return render_template('product/shop_women.html', products=products)

@product_bp.route('/shop/accessories')
def shop_accessories():
    # Fetch accessories from the database
    products = Product.query.filter_by(category="accessories").all()
    return render_template('product/shop_accessories.html', products=products)