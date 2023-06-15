from flask import Flask, request
import pymysql
import db_connector
import rest_app
import os
import signal

app = Flask(__name__)

@app.route('/users/get_user_name/<user_id>',methods=['GET'])
def get_user_name(user_id):
    #check if the user is in the database
    name = db_connector.get_users_names(user_id)
    if name!=None:
        return f'<H1 id="name"> {name[0]} </H1>'
    return f'<H1 id="error">no such user: {user_id} </H1>'

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(),signal.CTRL_C_EVENT)
    return 'Server stopped'



if __name__=="__main__":
    app.run(host='127.0.0.1', debug=True, port=5500)