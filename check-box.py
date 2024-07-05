import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class democheckbox():
    def getcheckboxes(self):
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=option)
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']").click()
        time.sleep(4)
        #driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()
        #time.sleep(4)
        driver.find_element(By.XPATH, "//a[normalize-space()='Senior Citizen']").click()
        time.sleep(4)
        var1 = driver.find_element(By.XPATH, "//a[normalize-space()='Armed Forces']").is_selected()
        print(var1)

checkboxes=democheckbox()
checkboxes.getcheckboxes()