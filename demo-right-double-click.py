import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class demortdblclk():
    def rtclk(self):
        driver=webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(4)
        # to right click
        '''achains=ActionChains(driver)
        ele1=driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        achains.context_click(ele1).perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
        time.sleep(4)'''

        achains=ActionChains(driver)
        ele2=driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(ele2).perform()
        time.sleep(4)
rightclk=demortdblclk()
rightclk.rtclk()