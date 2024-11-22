from flask import request, render_template ,session
from app import app
from follow.followLogic import followLogic

@app.route("/follow",methods = ['POST'])
def followControllerFunction():
    followLogicObj = followLogic()
    data = request.json
    userId = session['userInfo']['userId']
    followerId = data.get("userId")
    return followLogicObj.followLogicFunction(userId,followerId)