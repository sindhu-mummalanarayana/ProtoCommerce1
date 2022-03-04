from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self,driver):
        self.driver=driver

    #self.driver.find_element(By.NAME, "name").send_keys("Sindhu")
    name=(By.NAME,"name")

    def name_signup_page(self):
        return self.driver.find_element(*SignUp.name)


    #self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("sindhu.suprith@gmail.com")
    email=(By.CSS_SELECTOR,"input[name='email']")
    def email_signup_page(self):
        return self.driver.find_element(*SignUp.email)
    #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("dummy")
    password=(By.ID,"exampleInputPassword1")
    def password_signup_page(self):
        return self.driver.find_element(*SignUp.password)
    #self.driver.find_element(By.ID, "exampleCheck1").click()
    love_icecream_checkbox=(By.ID,"exampleCheck1")
    def love_icecream_checkbox_signup_page(self):
        return self.driver.find_element(*SignUp.love_icecream_checkbox)

    #Select(self.driver.find_element(By.ID, "exampleFormControlSelect1")).select_by_visible_text("Female")
    gender=(By.ID,"exampleFormControlSelect1")
    def gender_signup_page(self):
        return self.driver.find_element(*SignUp.gender)
#employmentStatus_student = self.driver.find_element(By.ID, "inlineRadio1")
    employmentStatus_student=(By.ID,"inlineRadio1")
    def employmentStatus_student_signup_page(self):
        return self.driver.find_element(*SignUp.employmentStatus_student)


    def get_home_page_title(self):
        return self.driver.title

    main_menu_list=(By.CSS_SELECTOR,"ul[class='navbar-nav'] li")

    def get_main_menu_list_main_page(self):
        return self.driver.find_elements(*SignUp.main_menu_list)

#self.driver.find_element(By.NAME, "bday").send_keys("12/12/1980")




#self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()