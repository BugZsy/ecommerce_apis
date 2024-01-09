from flask import Blueprint, request
from controllers import search_product_controllers

search_routes = Blueprint('search_routes',__name__)

@search_routes.route('/search_by_name',methods = ['POST'])
def search_by_name():
    data = request.form
    return search_product_controllers.search_by_name_controller(data)

@search_routes.route('/search_by_category',methods = ['POST'])
def search_by_category():
    data = request.form
    return search_product_controllers.search_by_category_controller(data)

