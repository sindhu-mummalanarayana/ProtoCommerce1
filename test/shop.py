from time import sleep

import catch as catch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
cart=[]
product=[]
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.element_to_be_clickable(driver.find_element(By.LINK_TEXT,"Shop")))
driver.find_element(By.LINK_TEXT,"Shop").click()
phone_models=driver.find_elements_by_xpath("//div[@class='card h-100']")
items_to_be_added_to_cart=['iphone X','Blackberry']
for phone in phone_models:
    model=(phone.find_element_by_xpath("div/h4/a").text)
    if model in items_to_be_added_to_cart:
        phone.find_element_by_xpath("div[2]/button").click()
        cart.append(model)
#print(cart)
driver.find_element(By.PARTIAL_LINK_TEXT,"Checkout").click()

checkout_items=driver.find_elements(By.XPATH,"//td[@class='col-sm-8 col-md-6']")
for item in checkout_items:
    product.append((item.find_element(By.XPATH,"div/div/h4/a").text))

driver.find_element(By.XPATH,"//button[contains(text(),'Checkout')]").click()
#print(product)
assert cart==product

driver.find_element(By.ID,"country").send_keys("IND")
wait=WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
success_confirmation =driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in success_confirmation
driver.get_screenshot_as_file("order_conirmation.png")