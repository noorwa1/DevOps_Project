from flask import request, Blueprint, jsonify
import db_connector
from datetime import datetime as time
REST = Blueprint('REST_API', __name__, template_folder='templates')

@REST.route('/users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == "GET":
        return get_request(user_id)
    elif request.method == "POST":
        return post_request(user_id)
    elif request.method == "PUT":
        return put_request(user_id)
    elif request.method == "DELETE":
        return delete_request(user_id)
    return None

def get_request(user_id):
    #get the user name from the database
    name = db_connector.get_users_names(user_id)
    #check if the get function returned a value and not None
    if name is not None:
        #in case there is a value do>
        return jsonify({'user_name': name, 'ID': user_id})
    #incase name is None >
    return jsonify({'status': "error", 'reason': "no such id"}), 500

def post_request(user_id):
    data=request.json
    flag=db_connector.save_user_data(user_id,data["user_name"],time.now())
    code_status=None
    if flag==True:
        payload={"status":"ok","user_added":data["user_name"]}
        code_status=200
    else:
        payload = {"status": "error", "reason": "id already exist"}
        code_status=500
    return jsonify(payload),code_status

def put_request(user_id):
    data = request.json
    code_status=None
    old_user_name=db_connector.get_users_names(user_id)
    flag=db_connector.get_users_names(user_id)
    if flag is not None:
        flag=db_connector.modify_user(user_id,data["user_name"])
        if flag==True:
            payload={'status':"ok",'user_updated':old_user_name}
            code_status=200
    else:
        payload={"status":"error","reason":"no such id"}
        code_status=500
    return payload,code_status

def delete_request(user_id):
    user_to_delete=db_connector.get_users_names(user_id)
    flag=db_connector.delete_user(user_id)
    code_status=None
    if flag==True:
        payload={"status":"ok","user_deleted":user_to_delete}
        code_status=200
    elif flag==False:
        payload={"status":"error","reason":"no such id"}
        code_status=500
    return jsonify(payload),code_status