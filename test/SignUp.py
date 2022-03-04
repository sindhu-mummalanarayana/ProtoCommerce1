from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("Sindhu")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("sindhu.suprith@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("dummy")
driver.find_element(By.ID,"exampleCheck1").click()
Select(driver.find_element(By.ID,"exampleFormControlSelect1")).select_by_visible_text("Female")
employmentStatus_student=driver.find_element(By.ID,"inlineRadio1")
employmentStatus_student.click()
assert employmentStatus_student.is_selected()

driver.find_element(By.NAME,"bday").send_keys("12/12/1980")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
driver.get_screenshot_as_file("Signup_success.png")


driver.close()




