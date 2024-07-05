
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class demoexplicitwait():
    def p2(self):
        driver = webdriver.Chrome()
        driver.get('https://www.yatra.com/')
        wait=WebDriverWait(driver, 15)
        departto=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departto.click()
        departto.send_keys("New Delhi")
        departto.send_keys(Keys.ENTER)

        goingto=driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        goingto.click()
        goingto.send_keys("New")
        searchresults=driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(searchresults))
        for result in searchresults:
            if "New York (JFK)" in result.text:
                result.click()
                #time.sleep(4)
                break

        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")).click()
        #driver.find_element(By.XPATH, "//td[@id='23/07/2024']").click()'''



        #aldates=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")))
        aldates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
        for date in aldates:
            if date.get_attribute("data-date") == '30/6/2024':
                date.click()
                break
        driver.implicitly_wait(5)

a1=demoexplicitwait()
a1.p2()

