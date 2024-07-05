from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class webcheck():
    def tectchk(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.maximize_window()
        l1=driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
        l1.click()
        l1.send_keys("Cham")
        #l1.send_keys(Keys.ENTER)
        time.sleep(4)

        driver.quit()

l22=webcheck()
l22.tectchk()
