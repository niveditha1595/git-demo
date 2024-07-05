import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class gettext():

    def get_text(self):
        option = Options()
        option.add_argument('--disable-notifications')
        driver= webdriver.Chrome(options=option)
        driver.get("https://www.yatra.com/")
        trt=driver.find_element(By.XPATH, "//a[@title='Spiritual Divine Yatra']//img[@class='conta iner large-banner']").text
        print(trt)
        time.sleep(8)

gttext = gettext()
gttext.get_text()
