import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class demogetattributevalue():
       def demo_getvalue(self):
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=option)
        driver= webdriver.Chrome()
        driver.get("https://www.yatra.com")
        attr = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr)
        time.sleep(8)

demogetattr = demogetattributevalue()
demogetattr.demo_getvalue()
