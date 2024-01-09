from models import search_product_models
from flask import jsonify
search_pro_obj = search_product_models.search_product_models()

def search_by_name_controller(data):
    if str(data.get('name')) == False:
        return jsonify({'Message':'Invalid name format'})
    return search_pro_obj.search_by_name_model(data)

def search_by_category_controller(data):
    if data.get('category').isalpha() == False:
        return jsonify({'Message':'Invalid Category format'})
    return search_pro_obj.search_by_category_model(data)
