from models import database
from flask import jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash

cursor = database.database_connection().create_cursor()
conn = database.database_connection.conn

class account_models():
    def __init__(self):
        pass

    def create_account_model(self,data):
        def check_if_user_exists():
            cursor.execute(
            '''
                SELECT username FROM users
                WHERE username = %s
            ''',(data.get('username'),)
            )
            user_exists = cursor.fetchone()
            if user_exists:
                return True
            
        if check_if_user_exists():
            return jsonify({'Message':'Account Already Exists. Log into Account with Credentials'})

        cursor.execute(
        '''
            INSERT INTO users (username,password)
            VALUES (%s,%s)
        ''',(data.get('username'),generate_password_hash(data.get('password')))
        )
        conn.commit()
        return jsonify({'Message':'Account Created Successfully'})
    
    def login_model(self,data):
        cursor.execute(
        '''
            SELECT user_id, password FROM users
            WHERE username = %s
        ''',(data.get('username'),)
        )
        user_exists = cursor.fetchone()
        if user_exists == None:
            return jsonify({'Message':'Account_does_not_exists'})
        if check_password_hash(user_exists[1],data.get('password')) == True:
            session['user_id'] = str(user_exists[0])
            print('user id stored in session')
            print(session['user_id'])
            print(type(session['user_id']))
            return jsonify({'Message':'Successful Login'})
        return jsonify({'Message':'Invalid login Credentials'})
    
    def logout_model(self):
        session.pop('user_id',None)
        return jsonify({'Message':'Logout Successful'})
    
    