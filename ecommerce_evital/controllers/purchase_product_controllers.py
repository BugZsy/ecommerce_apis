from models import purchase_product_models
from flask import jsonify
pur_pro_obj = purchase_product_models.purchase_product_models()

def buy_products_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid product_id format'})
    if data.get('quantity_to_buy').isdigit() == False:
        return jsonify({'Message':'Invalid quantity format'})
    return pur_pro_obj.buy_products_model(data)

def add_to_cart_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid product_id format'})
    if data.get('quantity_to_buy').isdigit() == False:
        return jsonify({'Message':'Invalid quantity format'})
    return pur_pro_obj.add_to_cart_model(data)

def delete_from_cart_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid product_id format'})
    return pur_pro_obj.delete_from_cart_model(data)

def update_cart_controller(data):
    if data.get('updated_quantity').isdigit() == False:
        return jsonify({'Message':'Invalid quantity Format'})
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid product id format'})
    return pur_pro_obj.update_cart_model(data)

def buy_from_cart_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid product_id format'})
    return pur_pro_obj.buy_from_cart_model(data)
