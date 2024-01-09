from models import account_models
from flask import jsonify
import re
acc_model_obj = account_models.account_models()

def create_account_controller(data):
    if data.get('username').isalpha() == False:
        return jsonify({'Message':'Invalid Username format. Username must contain characters only'})
    if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$",data.get('password')) == None or (' ' in data.get('password')):
        return jsonify({'Invalid password format': 'Needs at Least 1 special Character, 1 Digit, 1 capital character, 1 small character and Length between 8 to 20 character and field cannot be blank'})
    return acc_model_obj.create_account_model(data)

def login_controller(data):
    if data.get('username').isalpha() == False:
        return jsonify({'Message':'Invalid Username format. Username must contain characters only'})
    if ' ' in data.get('password'):
        return jsonify({'Message':'Invalid password format'})
    return acc_model_obj.login_model(data)

def logout_controller():
    return acc_model_obj.logout_model()