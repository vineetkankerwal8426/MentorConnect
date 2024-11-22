import mysql.connector
from flask import jsonify

class sessionRequestLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def sessionRequestAcceptFuction(self,reqid,sessionlink):
        query1 = f"SELECT * from sessionrequests where reqid = '{reqid}'"
        self.cur.execute(query1)
        sessionrequest_info = self.cur.fetchone()
        print(sessionrequest_info)
        return "succes"