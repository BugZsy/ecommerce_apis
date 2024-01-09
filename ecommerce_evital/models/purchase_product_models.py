from models import database
from flask import jsonify
from models.account_models import session

cursor = database.database_connection().create_cursor()
conn = database.database_connection.conn

class purchase_product_models():
    def __init__(self):
        pass

    def buy_products_model(self,data):
        cursor.execute(
        '''
        SELECT quantity FROM products
        WHERE product_id = %s
        ''',(data.get('product_id'),)
        )
        
        quantity = cursor.fetchone()
        try:
            if quantity[0] <= 0:
                return jsonify({'Message':'Product Not available'})
        except:
            return jsonify({'Message':'Product is not available'})
        if quantity[0] < int(data.get('quantity_to_buy')):
            return jsonify({'Message':'Selected Quantity is Not Available'})
        
        cursor.execute(
        '''
            UPDATE products
            SET quantity = quantity - %s
            WHERE product_id = %s
        ''',(int(data.get('quantity_to_buy')),data.get('product_id'))
        )
        conn.commit()
        cursor.execute(
        '''
        INSERT INTO orders (user_id, product_id, quantity)
        VALUES (%s, %s, %s) RETURNING user_id, product_id, quantity
        ''',(session.get('user_id'),data.get('product_id'),data.get('quantity_to_buy'))
        )
        conn.commit()
        pur_pro_details = cursor.fetchone()
        return jsonify({'Product Purchased successfully':pur_pro_details})
    
    def add_to_cart_model(self,data):
        cursor.execute(
        '''
            SELECT cart_id FROM shopping_cart
            WHERE user_id = %s AND product_id = %s
        ''',(session.get('user_id'),data.get('product_id'),)
        )
        prod_in_cart = cursor.fetchone()
        if prod_in_cart:
            return jsonify({'Message':'Product already in cart'})
        
        cursor.execute(
        '''
            INSERT INTO shopping_cart (user_id, product_id, quantity)
            VALUES (%s, %s, %s) RETURNING user_id, product_id, quantity
        ''',(session.get('user_id'), data.get('product_id'),data.get('quantity_to_buy'))
        )
        conn.commit()
        cart_item = cursor.fetchone()
        return jsonify({'Product added to cart successfully':cart_item})
    
    def delete_from_cart_model(self,data):
        cursor.execute(
        '''
            DELETE FROM shopping_cart
            WHERE user_id = %s AND product_id = %s RETURNING user_id, product_id, quantity
        ''',(session.get('user_id'),data.get('product_id'))
        )
        conn.commit()
        removed_from_cart = cursor.fetchone()
        if removed_from_cart:
            return jsonify({'Product Removed from cart':removed_from_cart})
        return jsonify({'Message':'Product is not in cart'})
    
    def update_cart_model(self,data):
        cursor.execute(
        '''
            UPDATE shopping_cart
            SET quantity = %s
            WHERE user_id = %s AND product_id = %s RETURNING user_id, product_id, quantity
        ''',(data.get('updated_quantity'),session.get('user_id'),data.get('product_id'))
        )
        conn.commit()
        updated_cart = cursor.fetchone()
        return jsonify({'cart updated successfully':updated_cart})
    
    def buy_from_cart_model(self,data):
        cursor.execute(
        '''
            DELETE FROM shopping_cart
            WHERE user_id = %s AND product_id = %s RETURNING user_id, product_id, quantity
        ''',(session.get('user_id'),data.get('product_id'))
        )
        conn.commit()
        bought_from_cart = cursor.fetchone()
        if bought_from_cart:
            cursor.execute(
            '''
                INSERT into orders (user_id, product_id, quantity)
                VALUES (%s,%s,%s) RETURNING user_id, product_id, quantity
            ''',(bought_from_cart[0],bought_from_cart[1],bought_from_cart[2])
            )
            conn.commit()
            pur_pro_details = cursor.fetchone()
            return jsonify({'Product Purchased successfully':pur_pro_details})
        return jsonify({'Message':'Product is not in cart'})