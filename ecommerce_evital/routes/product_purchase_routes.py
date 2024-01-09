from flask import Blueprint, request, jsonify
from functools import wraps
from models.account_models import session
from controllers import purchase_product_controllers

def logged_in(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'Message': 'Login Required'}), 401
        else:
             return f(*args, **kwargs)
    return decorated_func

purchase_product_routes = Blueprint('purchase_product_routes',__name__)

@purchase_product_routes.route('/buy_products',methods = ["POST"])
@logged_in
def buy_products():
    data = request.form
    return purchase_product_controllers.buy_products_controller(data)
    

@purchase_product_routes.route('/add_to_cart',methods = ['POST'])
@logged_in
def add_to_cart():
    data = request.form
    return purchase_product_controllers.add_to_cart_controller(data)

@purchase_product_routes.route('/delete_from_cart',methods = ['POST'])
@logged_in
def delete_from_cart():
    data = request.form
    return purchase_product_controllers.delete_from_cart_controller(data)

@purchase_product_routes.route('/update_cart',methods = ['POST'])
@logged_in
def update_cart():
    data = request.form
    return purchase_product_controllers.update_cart_controller(data)

@purchase_product_routes.route('/buy_from_cart',methods = ['POST'])
@logged_in
def buy_from_cart():
    data = request.form
    return purchase_product_controllers.buy_from_cart_controller(data)