import pymysql

conn= pymysql.connect(host="127.0.0.1",port=3306,user="root",db="first_project")

#This function is for combained testing
def get_all_data(user_id):
    data=()
    my_cursor = conn.cursor()
    #get the data from the database
    my_cursor.execute("SELECT * FROM Users WHERE ID={};".format(user_id))
    #take the data(it will be a tuple)
    data=my_cursor.fetchall()
    my_cursor.close()
    try:
       return data[0]
    except Exception :
        return None


def get_users_names(user_id):
    data=()
    my_cursor = conn.cursor()
    #get the data from the database
    my_cursor.execute("SELECT user_name FROM Users WHERE ID={};".format(user_id))
    #take the data(it will be a tuple)
    data=my_cursor.fetchall()
    my_cursor.close()
    try:
       return data[0]
    except Exception :
        return None

def save_user_data(user_id,name,date):
    my_cursor = conn.cursor()
    try:
        my_cursor.execute("INSERT INTO users (id,user_name,creation_date) VALUES ({},'{}','{}');".format(user_id,name,date))
        conn.commit()
        my_cursor.close()
    except Exception:
        return False
    return True

def delete_user(user_id):
    my_cursor=conn.cursor()
    try:
        my_cursor.execute(("DELETE FROM users WHERE id={};").format(user_id))
        conn.commit()
        my_cursor.close()

    except Exception:
        return False
    return True

def modify_user(user_id,user_name):
    my_cursor=conn.cursor()
    try:
        my_cursor.execute(("UPDATE users SET user_name = '{}' WHERE id = {}").format(user_name,user_id))
        conn.commit()
        my_cursor.close()

    except Exception:
        return False
    return True

