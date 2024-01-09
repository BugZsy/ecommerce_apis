from flask import Blueprint, request
from controllers import account_controllers
account_routes = Blueprint('account_blueprint',__name__)

@account_routes.route('/create_account',methods = ['POST'])
def create_account():
    data = request.form
    return account_controllers.create_account_controller(data)

@account_routes.route('/login',methods = ['POST'])
def login():
    data = request.form
    return account_controllers.login_controller(data)

@account_routes.route('/logout',methods = ['POST'])
def logout():
    return account_controllers.logout_controller()