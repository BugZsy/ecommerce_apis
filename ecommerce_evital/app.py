from flask import Flask
from routes.account_routes import account_routes
from routes.search_product_routes import search_routes
from routes.product_purchase_routes import purchase_product_routes
from routes.CUD_routes import CUD_routes

app = Flask(__name__)
app.secret_key = 'precious_secret_key'
app.register_blueprint(account_routes,url_prefix = '/Home')
app.register_blueprint(search_routes,url_prefix = '/Home/search')
app.register_blueprint(purchase_product_routes, url_prefix = '/Home/search/products')
app.register_blueprint(CUD_routes,url_prefix = '/admin')

if __name__ == '__main__':
    app.run(debug=True)
