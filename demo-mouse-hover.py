import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class demomouseover():
    def mouvr(self):
        driver=webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebut=driver.find_element(By.XPATH, "//span[@class='more-arr']")
        myacclink=driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        ach=ActionChains(driver)
        ach.move_to_element(myacclink).perform()  # perform is important, without that we can't perform any action
        time.sleep(5)
        ach.move_to_element(morebut).perform()   # perform is important, without that we can't perform any action
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@id='booking_engine_cruise']").click()
        time.sleep(5)


mmh=demomouseover()
mmh.mouvr()

