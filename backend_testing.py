from seleniumrequests import Chrome
import db_connector
webdriver=Chrome()
req_method='POST'

#sends a post request through webdriver which returns a json response
response= webdriver.request(req_method,'http://127.0.0.1:5500/users/8',json={'id':8,'user_name':"asd"})
#evaluate the response text so we can start using the response data
request_data=eval(response.text)
try:
    #sending a GET request
    GET_response=webdriver.request('GET','http://127.0.0.1:5500/users/8')
    if request_data['user_added']==db_connector.get_users_names(8)[0] and request_data['status']=='ok' and GET_response.status_code==200:
        print("The data has been sent successfully!")

except :
    print('something went wrong')