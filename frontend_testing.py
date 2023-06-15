from selenium.webdriver.common.by import By
from selenium import webdriver
import os

s=os.path.abspath("chromedriver.exe")

ss=s.replace('\\',"/")

driver = webdriver.Chrome(ss)

driver.get("http://127.0.0.1:5500/users/get_user_name/2")

try:
    id_element=driver.find_element(By.ID,value="name")
    print(id_element.text)

except Exception as e:
    print(e.with_traceback())
