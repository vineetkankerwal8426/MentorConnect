import mysql.connector
from flask import jsonify,session
class loginLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def loginLogicFunction(self,email,password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.cur.execute(query, (email, password))
        user_info = self.cur.fetchone()

        if user_info:
        # Exclude the password from the response
            user_info.pop('password')
            session['userInfo'] = user_info
            print(session['userInfo'],"from loginlogic")
            return jsonify({'status': 'success', 'user_info': user_info}), 200
        else:
            return jsonify({'status': 'fail', 'message': 'Invalid email or password'}), 401