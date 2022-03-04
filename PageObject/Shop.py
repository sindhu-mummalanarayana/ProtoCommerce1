
from selenium.webdriver.common.by import By

class Shop:
    def __init__(self,driver):
        self.driver=driver

    #self.driver.find_element(By.NAME, "name").send_keys("Sindhu")
    shop=(By.LINK_TEXT,"Shop")
    wait