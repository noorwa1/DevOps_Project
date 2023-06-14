from seleniumrequests import Chrome
import db_connector
from selenium.webdriver.common.by import By
webdriver=Chrome()
POST_response= webdriver.request('POST','http://127.0.0.1:5500/users/9',json={'id':9,'user_name':"engld"})
GET_response= webdriver.request('GET','http://127.0.0.1:5500/users/9')
posted_data=eval(POST_response.text)
data_from_DB=db_connector.get_all_data(9)

try:
    if GET_response.status_code!=200:
        print("something went wrong code error: {}".format(GET_response))
        raise Exception('test faild')
    if posted_data['user_added']!=data_from_DB[1] or data_from_DB[0]!=9 :
        raise Exception('test faild')
    print("everything went well")
except :
    print(Exception.with_traceback())

webdriver.get('http://127.0.0.1:5500/users/get_user_name/{}'.format(data_from_DB[0]))
id_element=webdriver.find_element(By.ID,value='name')
if id_element.text!=data_from_DB[1]:
    raise Exception("test faild")