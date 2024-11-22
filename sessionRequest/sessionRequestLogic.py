import mysql.connector
from flask import jsonify,session

class sessionRequestLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def sessionRequestAcceptFunction(self,reqid,sessionlink):
        try:
            query1 = f"SELECT * from sessionrequests where reqid = '{reqid}'"
            self.cur.execute(query1)
            sessionrequest_info = self.cur.fetchone()

            query2 = "insert into sessions (sessionTopic,sessionDate,sessionTime,sessionLink,userId,mentorId,sessionMessage) values (%s,%s,%s,%s,%s,%s,%s)"
            self.cur.execute(query2, (sessionrequest_info['sessionTopic'],sessionrequest_info['sessionDate'],sessionrequest_info['sessionTime'],sessionlink,sessionrequest_info['userId'],sessionrequest_info['mentorId'],sessionrequest_info['sessionMessage']))
            self.con.commit()

            query3 = f"delete from sessionrequests where reqid = '{reqid}'"
            self.cur.execute(query3)
            self.con.commit()

            return jsonify({'status': 'success'})
            # print(sessionrequest_info)
            # return "hello"
        except:
            return jsonify({'status': 'fail'}), 401
        
    def sessionRequestRejectFunction(self,reqid):
        query = f"delete from sessionrequests where reqid = {reqid}"
        try:
            self.cur.execute(query)
            self.con.commit()
            return jsonify({'status': 'success'})
        except:
            return jsonify({'status': 'fail'}), 401
        
    def requestSessionFunction(self,mentorIdname,sessionDate,sessionTime,sessionTopic,sessionMessage):
        sessionUserInfo = session.get("userInfo")
        try:
            query1 = f"select userid from users where useridname = '{mentorIdname}'"
            print(mentorIdname)
            self.cur.execute(query1)
            mentorId = self.cur.fetchone()
            
            query2 = "insert into sessionrequests (userId,mentorId,sessionDate,sessionTime,sessionTopic,sessionMessage) values (%s,%s,%s,%s,%s,%s)"
            self.cur.execute(query2,(sessionUserInfo['userId'],mentorId["userid"],sessionDate,sessionTime,sessionTopic,sessionMessage))
            self.con.commit()
            return jsonify({'status': 'success'})
        except:
            return jsonify({'status': 'fail'}), 401