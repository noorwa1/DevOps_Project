from selenium.webdriver.common.by import By
from selenium import webdriver


driver=webdriver.Chrome(service=Service("C:\\Users\\noorw\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("http://127.0.0.1:5501/users/get_user_name/2")

try:
    id_element=driver.find_element(By.ID,value="name")
    driver.implicitly_wait(10)
    print(id_element.text)

except Exception as e:
    print("error",e.with_traceback)
