import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class demodragdrop():
    def demodd(self):
        driver=webdriver.Chrome()
        '''driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1=driver.find_element(By.XPATH, "//div[@id='draggable']")
        elem2=driver.find_element(By.XPATH, "//div[@id='droppable']")
        #ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 70, 80).perform()
        time.sleep(5)'''

        driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
        elem1=driver.find_element(By.XPATH, "//div[@id='box7']")
        elem2=driver.find_element(By.XPATH, "//div[@id='box107']")
        ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        time.sleep(5)

p2=demodragdrop()
p2.demodd()
