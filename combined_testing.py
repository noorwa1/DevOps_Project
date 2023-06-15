from selenium.webdriver.chrome.service import Service
from seleniumrequests import Chrome
import db_connector
from selenium.webdriver.common.by import By
from selenium import webdriver as drive
webdriver=Chrome()
id=10

POST_response = webdriver.request('POST',f'http://127.0.0.1:5500/users/{id}',json={'id':id,'user_name':"engld"})
GET_response= webdriver.request('GET',f'http://127.0.0.1:5500/users/{id}')
posted_data=eval(POST_response.text)
data_from_DB=db_connector.get_all_data(id)

try:
    if GET_response.status_code!=200:
        print("something went wrong code error: {}".format(GET_response))
        raise Exception('test faild')
    if posted_data['user_added']!=data_from_DB[1] or data_from_DB[0]!=id :
        raise Exception('test faild')
    print("everything went well")
except :
    print(Exception.with_traceback())



'''
#geting the path of the chrome driver
options = drive.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
options.add_argument("chromedriver.exe")  # Path to the chromedriver executable
driver = drive.Chrome(options=options)
'''
driver=drive.Chrome(service=Service("C:/Users/noorw/Downloads/chromedriver_win32/chromedriver.exe"))
driver.get(f'http://127.0.0.1:5501/users/get_user_name/"{data_from_DB[0]}"')
id_element=driver.find_element(By.ID,value='name')
print(id_element.text)
if id_element.text!=data_from_DB[1]:
    raise Exception("test faild")
