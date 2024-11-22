import mysql.connector
from flask import jsonify,session
from datetime import timedelta

class userProfileLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def userProfileFunction(self,idname):
        query1 = f"SELECT firstname,email,userIdName FROM users WHERE userIdName = '{idname}'"
        print(query1)
        self.cur.execute(query1)
        user_info = self.cur.fetchone()
        if user_info == None:
            return "user Not Found"
        query2 = f"select USERBIO from userinformation natural join users where users.useridname = '{idname}'"
        self.cur.execute(query2)
        user_info.update(self.cur.fetchone())

        query3 = f"select sessiontopic, sessiondate,sessiontime,sessionlink from sessions join users where (sessions.userid = users.userid or sessions.mentorid = users.userid) and users.useridname = '{idname}'"
        self.cur.execute(query3)
        results = self.cur.fetchall()
        print(results)
        sessions = []
        for row in results:
            sessiontopic=row['sessiontopic']
            sessiondate= row['sessiondate']
            sessiontime = row['sessiontime']
            sessionlink = row['sessionlink']
            print(sessiontopic)
            # Convert `timedelta` to string
            if isinstance(sessiontime,timedelta):
                sessiontime = str(sessiontime)
    
            sessions.append({
                "sessiontopic": sessiontopic,
                "sessiondate": sessiondate,  # Convert to ISO format
                "sessiontime": sessiontime,
                "sessionlink":sessionlink
            })

        user_info["sessions"] = sessions
        sessionUserInfo = session.get("userInfo")
        if(sessionUserInfo == None):  #user is not loggedIn
            user_info["sessionsRequests"] = False
            user_info["sessionRequestButton"] = False
            user_info['followRequestButton'] =False
            return user_info
    
        elif(sessionUserInfo["userIdName"]!=idname): #user is loggedIn but want to see profile of any other user
            user_info["sessionsRequests"] = False
            user_info["sessionRequestButton"] = True
            user_info['followRequestButton'] = True
            return user_info
        
        #user is loggedIn and want to see its own profile
        query4 = f"select reqId,useridname,sessionTopic,sessionDate,sessionTime,sessionMessage from sessionrequests natural join users where mentorId = (select userId from users where useridname = '{idname}');"
        self.cur.execute(query4)
        results = self.cur.fetchall()
        sessionsReq = []
        for row in results:
            sessionrequestid = row['reqId']
            useridname = row['useridname']
            sessiontopic=row['sessionTopic']
            sessiondate= row['sessionDate']
            sessiontime = row['sessionTime']
            sessionmessage = row['sessionMessage']
       
            # Convert `timedelta` to string
            if isinstance(sessiontime,timedelta):
                sessiontime = str(sessiontime)
    
            sessionsReq.append({
                "sessionrequestid":sessionrequestid,
                "useridname":useridname,
                "sessiontopic": sessiontopic,
                "sessiondate": sessiondate,  # Convert to ISO format
                "sessiontime": sessiontime,
                "sessionmessage":sessionmessage
            })

        user_info["sessionsRequests"] = sessionsReq
        user_info["sessionRequestButton"] = False
        user_info['followRequestButton'] =False
        return user_info