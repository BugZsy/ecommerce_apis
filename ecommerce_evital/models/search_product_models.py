from models import database
from flask import jsonify

cursor = database.database_connection().create_cursor()
conn = database.database_connection.conn

class search_product_models():
    def __init__ (self):
        pass

    def search_by_name_model(self,data):
        Path = "https://firebasestorage.googleapis.com/v0/b/evitalproductstorage.appspot.com/o/evital_task_products%2F"
        cursor.execute(
        '''
           SELECT name, description, price, category, prod_img_links FROM products
           WHERE name ILIKE %s
        ''',('%' + data.get('name') + '%',)
        )
        prods = cursor.fetchall()
        new_prods_list = []

        for prod_tuple in prods:
            prod_dict = {
                'name': prod_tuple[0],
                'description': prod_tuple[1],
                'price': prod_tuple[2],
                'category': prod_tuple[3],
                'prod_img_links': Path + prod_tuple[4]
            }
            new_prods_list.append(prod_dict)
        return jsonify({'products': new_prods_list})

    def search_by_category_model(self,data):
        Path = "https://firebasestorage.googleapis.com/v0/b/evitalproductstorage.appspot.com/o/evital_task_products%2F"
        cursor.execute(
        '''
             SELECT name, description, price, category, prod_img_links FROM products
             WHERE category = %s
        ''',(data.get('category'),)
        )
        prods = cursor.fetchall()
        new_prods_list = []

        for prod_tuple in prods:
            prod_dict = {
                'name': prod_tuple[0],
                'description': prod_tuple[1],
                'price': prod_tuple[2],
                'category': prod_tuple[3],
                'prod_img_links': Path + prod_tuple[4]
            }
            new_prods_list.append(prod_dict)
        return jsonify({'products': new_prods_list})
