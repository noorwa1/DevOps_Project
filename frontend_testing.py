from selenium.webdriver.common.by import By
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
options.add_argument("chromedriver.exe")  # Path to the chromedriver executable

driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:5501/users/get_user_name/2")

try:
    id_element=driver.find_element(By.ID,value="name")
    print(id_element.text)

except Exception as e:
    print(e.with_traceback)
