import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class demodropdown():
    def dropdowncheck(self):
        driver= webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdownn=driver.find_element(By.NAME, "UserTitle")
        sel=Select(dropdownn)
        sel.select_by_index(1)
        time.sleep(2)
        sel.select_by_visible_text("Operations Manager")
        time.sleep(2)
        #Select(sel).select_by_value("CxO_General_Manager_ANZ"): I could see attribute error. So to address this above method is followed
        #time.sleep(2)

ddp1 = demodropdown()
ddp1.dropdowncheck()

