from flask import Blueprint,request
from controllers import CUD_controllers

CUD_routes = Blueprint('CUD_routes',__name__)
@CUD_routes.route('/create_product',methods = ['POST'])
def create_product():
    data = request.form
    return CUD_controllers.create_product_controller(data)

@CUD_routes.route('/update_product_details',methods = ['POST'])
def update_product_details():
    data = request.form
    return CUD_controllers.update_product_details_controller(data)

@CUD_routes.route('/update_product_quantity',methods = ['POST'])
def update_product_quantity():
    data = request.form
    return CUD_controllers.update_product_quantity_controller(data)

@CUD_routes.route('/delete_product',methods = ['DELETE'])
def delete_product():
    data = request.form
    return CUD_controllers.delete_product_controller(data)