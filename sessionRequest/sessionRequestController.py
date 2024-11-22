from flask import request,session
from app import app
from sessionRequest.sessionRequestLogic import sessionRequestLogic



@app.route("/sessionaccepted",methods = ["POST"])
def sessionRequestAcceptedControllerFunc():
    sessionRequestLogicObj = sessionRequestLogic()
    data = request.json
    reqid = data.get("sessionrequestid")
    sessionlink = data.get('sessionlink')
    return sessionRequestLogicObj.sessionRequestAcceptFunction(reqid,sessionlink)

@app.route("/sessionrejected",methods=["DELETE"])
def sessionRequestRejectedControllerFunc():
    sessionRequestLogicObj = sessionRequestLogic()
    data = request.json
    reqid = data.get("sessionrequestid")
    return sessionRequestLogicObj.sessionRequestRejectFunction(reqid)

@app.route("/requestsession",methods=["POST"])
def requestSessionControllerFunction():
    sessionRequestLogicObj = sessionRequestLogic()
    data = request.json
    mentorIdname = data.get("mentorUserIdName")
    # print(mentorIdname)
    sessionDate = data.get("sessionDate")
    sessionTime = data.get("sessionTime")
    sessionTopic = data.get("sessionTopic")
    sessionMessage = data.get("sessionMessage")
    return sessionRequestLogicObj.requestSessionFunction(mentorIdname,sessionDate,sessionTime,sessionTopic,sessionMessage)
