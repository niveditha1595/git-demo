import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demomultiplewindows():
    def mulwindows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parhandle = driver.current_window_handle # to handle current window
        print(parhandle)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title='Spiritual Divine Yatra']//img[@class='conta iner large-banner']").click()
        time.sleep(5)
        alhandle = driver.window_handles # to handle all window
        print(alhandle)
        for handle in alhandle:
            if handle != parhandle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/india-tour-packages/holidays-in-ayodhya']//div[@class='Card']//span[contains(text(),'Book Now')]").click()
                time.sleep(4)
                driver.close()
                time.sleep(4)
                break
                driver.switch_to.window(parhandle)


mul=demomultiplewindows()
mul.mulwindows()
