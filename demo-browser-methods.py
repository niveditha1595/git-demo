import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class demoseleniumlearning():
    def demobrowsermethod(self):
        driver= webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)   # to print the used URL
        print(driver.title)     # to print the title of the website
        driver.maximize_window()  #to maximize the window
        driver.fullscreen_window()  # to enlarge screen
        driver.refresh()    # to refresh page
        driver.find_element(By.LINK_TEXT, 'ALL COURSES').click()
        driver.back()      # return one step back
        driver.forward()   # navigate to next page
        driver.minimize_window()  # to reduce the screen size
        time.sleep(20)
        driver.quit()

demobrowser = demoseleniumlearning()

demobrowser.demobrowsermethod()
