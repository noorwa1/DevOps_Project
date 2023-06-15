from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

'''
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
options.add_argument("chromedriver.exe")  # Path to the chromedriver executable
driver = webdriver.Chrome(options=options)
print(driver.title)
'''
driver = webdriver.Chrome(service=Service("C:\\Users\\noorw\\Downloads\\chromedriver_win32\\chromedriver.exe"))
driver.get("http://127.0.0.1:5501/users/get_user_name/2")

try:
    id_element=driver.find_element(By.ID,value="name")
    print(id_element.text)

except Exception as e:
    print("error",e.with_traceback)
