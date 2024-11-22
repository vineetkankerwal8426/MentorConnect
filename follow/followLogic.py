import mysql.connector
from flask import jsonify

class followLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def followLogicFunction(self,userId,followerId):
        query = "INSERT INTO follower (userId,followerId) VALUES (%s,%s)"
        try:
            self.cur.execute(query, (userId,followerId))
            self.con.commit()
            return jsonify({'status': 'success'}), 200
        except:
            return jsonify({'status': 'fail', 'message': 'failed while commiting query'}), 401