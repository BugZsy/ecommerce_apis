from models import database
from flask import jsonify
cursor = database.database_connection().create_cursor()
conn = database.database_connection.conn

class CUD_models():
    def __init__(self):
        pass

    def create_product_model(self,data):
        cursor.execute(
        '''
            SELECT product_id FROM products
            WHERE name = %s
        ''',(data.get('name'),)
        )
        prod_exists = cursor.fetchone()
        if prod_exists:
            return jsonify({'Message':'Product already exists'})
        
        cursor.execute(
        '''
            INSERT INTO products (name, description, price, category, quantity, prod_img_links)
            VALUES (%s,%s,%s,%s,%s,%s) RETURNING *
        ''',(data.get('name'),data.get('description'),data.get('price'),data.get('category'),data.get('quantity'),data.get('prod_img_links'))
        )
        conn.commit()
        new_prods = cursor.fetchone()

        return jsonify({'New Products added Successfully':new_prods})
    
    def update_product_details_model(self,data):
        cursor.execute(
        '''
            UPDATE products
            SET name = %s, description = %s, price = %s, category = %s, prod_img_links = %s
            WHERE product_id = %s RETURNING name, description, price, category, quantity
        ''',(data.get('name'),data.get('description'),data.get('price'),data.get('category'),data.get('prod_img_links'),data.get('product_id'))
        )
        conn.commit()

        updt_prods = cursor.fetchone()
        if updt_prods:
            return jsonify({'Updated Product Details':updt_prods})
        return jsonify({'Message':'Product does not exists'})
    
    def update_product_quantity_model(self,data):
        cursor.execute(
        '''
            UPDATE products
            SET quantity = %s
            WHERE product_id = %s RETURNING name, quantity
        ''',(data.get('quantity'),data.get('product_id'))
        )
        conn.commit()

        updt_quantity = cursor.fetchone()
        if updt_quantity:
            return jsonify({'Quantity Updated':updt_quantity})
        return jsonify({'Message':'Product does not exists'})
    
    def delete_product_model(self,data):
        cursor.execute(
        '''
            DELETE FROM products
            WHERE product_id = %s RETURNING *
        ''',(data.get('product_id'),)
        )
        conn.commit()

        del_prod = cursor.fetchone()
        if del_prod:
            return jsonify({'Product Deleted Successfully':del_prod})
        return jsonify({'Message':'Product does not exists'})
