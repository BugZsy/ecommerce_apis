from models import CUD_models
from flask import jsonify
CUD_model_obj = CUD_models.CUD_models()

def create_product_controller(data):
    if type(data.get('name')) != str:
        return jsonify({'Message':'Invalid name format'})
    if type(data.get('description')) != str:
        return jsonify({'Message':'Invalid description format'})
    if data.get('price').isdigit() == False:
        return jsonify({'Message':'Invalid price format'})
    if data.get('category').isalpha() == False:
        return jsonify({'Message':'Invalid category format'})
    if data.get('quantity').isdigit() == False:
        return jsonify({'Message':'Invalid quantity format'})
    if (' ' in  data.get('prod_img_links')) == True:
        return jsonify({'Message':'Invalid link format'})
    return CUD_model_obj.create_product_model(data)

def update_product_details_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid id format'})
    if type(data.get('name')) != str:
        return jsonify({'Message':'Invalid Name format'})
    if type(data.get('description')) != str:
        return jsonify({'Message':'Invalid description format'})
    if data.get('price').isdigit() == False or int(data.get('price')) <= 0:
        return jsonify({'Message':'Invalid price format'})
    if data.get('category').isalpha() == False:
        return jsonify({'Message':'Invalid category format'})
    return CUD_model_obj.update_product_details_model(data)     

def update_product_quantity_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid id format'})
    if data.get('quantity').isdigit() == False or int(data.get('quantity')) <= 0:
        return jsonify({'Message':'Invalid quantity format'})
    return CUD_model_obj.update_product_quantity_model(data)

def delete_product_controller(data):
    if data.get('product_id').isdigit() == False:
        return jsonify({'Message':'Invalid id format'})
    return CUD_model_obj.delete_product_model(data)