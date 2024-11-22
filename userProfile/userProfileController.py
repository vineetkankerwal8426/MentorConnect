from flask import request,session
from app import app
from userProfile.userProfileLogic import userProfileLogic

userProfileObj = userProfileLogic()
@app.route("/user/<idname>")
def userProfileControllerFunc(idname):
    # userInfo = session.get("userInfo")
    # userInfo == None or userInfo['userIdName']!= idname
    return userProfileObj.userProfileFunction(idname)