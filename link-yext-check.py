import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class loginpage():
    def locatebylnktext(self):
        option=Options()
        option.add_argument('--disable-notifications')
        driver= webdriver.Chrome(options=option)
        driver.get("https://www.yatra.com/")
        lista=driver.find_elements(By.TAG_NAME,'a')
        print(len(lista))   # text associated with elements
        for i in lista:
            print(i.text)
        time.sleep(5)

findbyid = loginpage()
findbyid.locatebylnktext()

