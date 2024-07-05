import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class demoslidercheck():
    def slidecheck(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/mobiles-power-banks?sort=plrty")
        driver.maximize_window()
        ele1= driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        ele2=driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(ele1, 60,0).perform()          # x axis is 60 and y axis is 0
        #ActionChains(driver).click_and_hold(ele1).pause(2).move_by_offset(70,0).release().perform()
        #ActionChains(driver).move_to_element(ele1).pause(2).click_and_hold(ele1).move_by_offset(100,0).release().perform()
        time.sleep(4)
        ActionChains(driver).drag_and_drop_by_offset(ele2, -40,0).perform()          # x axis is 60 and y axis is 0
        time.sleep(4)


p1=demoslidercheck()
p1.slidecheck()

