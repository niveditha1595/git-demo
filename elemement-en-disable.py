# URL used is : https://training.openspan.com/login

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demoenabled():
    def demogetena(self):
        driver= webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        l1=driver.find_element(By.ID, 'login_button').is_enabled()
        print(l1)
        driver.find_element(By.NAME, 'user_name').send_keys('test123@gmail.com')
        driver.find_element(By.NAME, 'user_pass').send_keys('123456')
        time.sleep(7)
        l1 = driver.find_element(By.ID, 'login_button').is_enabled()
        print(l1)
        time.sleep(8)

findbyid = demoenabled()
(findbyid.demogetena())
