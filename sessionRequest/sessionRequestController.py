from flask import request
from app import app
from sessionRequest.sessionRequestLogic import sessionRequestLogic



@app.route("/sessionaccepted",methods = ["POST"])
def sessionRequestControllerFunc():
    sessionRequestLogicObj = sessionRequestLogic()
    data = request.json
    reqid = data.get("sessionrequestid")
    sessionlink = data.get('sessionlink')
    return sessionRequestLogicObj.sessionRequestAcceptFuction(reqid,sessionlink)