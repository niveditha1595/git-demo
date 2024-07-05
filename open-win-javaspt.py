import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demoalertsjavascript():
    def demalertjs(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")  # name value
        # to accept value
        '''driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(4)
        
        # to dismiss the value:
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(4)'''

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.send_keys("good morning")
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(4)

demjjs=demoalertsjavascript()
demjjs.demalertjs()