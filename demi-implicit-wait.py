# Implicit-wait: Tells the webdriver maximum wait time when searching an element before throwing exception
# Implicit wait is applicable to all the webelements
# Explicit wait: Tell the webdriver to halt execution until a particular condition is met
# Explicit wait is applicable only to those webelements specified by the user

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demoimptwait():
    def implicheck(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)    # here it will wait till the specified time when it is difficult to find the web element
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "username").send_keys("niveditha122@gmail.com")
        time.sleep(5)
        #driver.find_element(By.ID, "usernamee").send_keys("niveditha122@gmail.com")


p1= demoimptwait()
p1.implicheck()