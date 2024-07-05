import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class demo_multiselect_dropdown():
    def multiselectdd(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        dd= driver.find_element(By.ID, 'multi-select')
        sel=Select(dd)
        sel.select_by_index(6)
        time.sleep(2)
        sel.select_by_value('Florida')
        sel.select_by_visible_text('New Jersey')
        sel.select_by_index(0)
        sel.select_by_visible_text('Ohio')
        time.sleep(5)

        sel.deselect_by_index(0)
        time.sleep(2)
        sel.deselect_by_value('Florida')
        time.sleep(2)
        sel.deselect_by_visible_text('Ohio')
        time.sleep(2)
        sel.deselect_all()
        time.sleep(2)

multidd=demo_multiselect_dropdown()
multidd.multiselectdd()