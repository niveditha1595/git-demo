import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demohidetoggle():
    def hide_toggle(self):
        driver= webdriver.Chrome()
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        l2=driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(l2)
        time(4)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        l2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(l2)
        time.sleep(6)
        

hidetoggle=demohidetoggle()
hidetoggle.hide_toggle()