import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class screnshotfile():
    def checkscrnshot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        srndemo=driver.find_element(By.ID, "login-continue-btn")
        srndemo.click()
        srndemo.screenshot('.//test.png')  # to save in current directory use . followed by 2 backward slash with file name
        time.sleep(4)

        driver.get_screenshot_as_file("C:/Users/Mahi7/PycharmProjects/practice_project/error.png")
        driver.save_screenshot(".//test1.png")


scrchec=screnshotfile()
scrchec.checkscrnshot()