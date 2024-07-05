import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class loginpage():
    def locatebyid(self):
        driver= webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, 'login-input').send_keys('test23@gmail.com')
        time.sleep(8)

findbyid = loginpage()
findbyid.locatebyid()
