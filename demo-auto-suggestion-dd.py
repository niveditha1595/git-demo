import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class demoautosuggestdropdown():
    def autodd(self):
        driver = webdriver.Chrome()
        driver.get('https://www.yatra.com/')
        departto=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departto.click()
        time.sleep(2)
        departto.send_keys("New Delhi")
        departto.send_keys(Keys.ENTER)
        time.sleep(2)

        goingto=driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        goingto.click()
        time.sleep(2)
        goingto.send_keys("New")
        searchresults=driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(searchresults))
        for result in searchresults:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break


        driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()      # for particular date
        time.sleep(9)
        #driver.find_element(By.XPATH, "//td[@id='23/07/2024']").click()
        #time.sleep(4)

        # for random date:
        aldates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
        for date in aldates:
            if date.get_attribute("data-date") == '30/6/2024':
                date.click()
                break

o12 = demoautosuggestdropdown()
o12.autodd()

