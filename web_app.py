from flask import Flask, request
import pymysql
from rest_app import REST
import db_connector
import rest_app
app = Flask(__name__)
app.register_blueprint(REST)

@app.route('/users/get_user_name/<user_id>',methods=['GET'])
def get_user_name(user_id):
    #check if the user is in the database
    name = db_connector.get_users_names(user_id)
    if name!=None:
        return f'<H1 id="name"> {name[0]} </H1>'
    return f'<H1 id="error">no such user: {user_id} </H1>'




if __name__=="__main__":
    app.run(host='127.0.0.1', debug=True, port=5500)