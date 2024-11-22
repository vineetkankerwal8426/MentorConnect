from flask import Flask, session 

app = Flask(__name__)
app.secret_key = "secret-key-Mentor-Connect"

import registration.registrationController
import login.loginController
import follow.followController
import userProfile.userProfileController
import sessionRequest.sessionRequestController

@app.route('/')
def mentorconnect():
    userInfo = session.get("userInfo")
    if(userInfo==None):
        session['userInfo'] = None

    return "welocome to MentorConnect"  



if __name__ == '__main__':
    app.run()