import mysql.connector
from flask import jsonify, render_template

class registerLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def register(self,firstName,middleName,lastName,email,phone,userIdName,password):
        query = "INSERT INTO USERS (FIRSTNAME,MIDDLENAME,LASTNAME,EMAIL,PHONE,USERIDNAME,PASSWORD) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cur.execute(query, (firstName,middleName,lastName,email,phone,userIdName, password))
            self.con.commit()
            return jsonify({'status': 'success'}), 200
        except mysql.connector.errors.IntegrityError:
            return "user name or email or phone already taken by someone else"
        except:
            return jsonify({'status': 'fail', 'message': 'failed while commiting query'}), 401