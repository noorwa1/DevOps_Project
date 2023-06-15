from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\noorw\\OneDrive\\Desktop\\web drivers\\chromedriver.exe")
driver.get("http://127.0.0.1:5500/users/get_user_name/2")

try:
    id_element=driver.find_element(By.ID,value="name")
    print(id_element.text)

except Exception as e:
    print(e.with_traceback())