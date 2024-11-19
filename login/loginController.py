from flask import request
from app import app
from login.loginLogic import loginLogic

loginObj = loginLogic()

@app.route("/login",methods = ['POST','GET'])
def loginControllerFuction():
    if(request.method == 'POST'):
        data = request.form
        email = data.get('email')
        password = data.get('password')
        return loginObj.loginLogicFunction(email,password)
    return "hello world from login"