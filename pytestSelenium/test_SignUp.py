import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.SignUp import SignUp
from utilities.BaseClass import BaseClass


class TestHome(BaseClass):
    def test_signUp_home_page(self):
        signup= SignUp(self.driver)
        signup.name_signup_page().send_keys("Sindhuiiiiiiiiiiiiiii")

        signup.email_signup_page().send_keys("sindhu.suprith@gmail.com")
        signup.password_signup_page().send_keys("dummy")
        signup.love_icecream_checkbox_signup_page().click()

        sel= Select(signup.gender_signup_page())
        sel.select_by_visible_text("Female")
        signup.employmentStatus_student_signup_page().click()
        assert signup.employmentStatus_student_signup_page().is_selected()

        #self.driver.find_element(By.NAME,"bday").send_keys("12/12/1980")
        #self.driver.find_element(By.XPATH,"//input[@value='Submit']").click()
        self.driver.get_screenshot_as_file("Signup_success.png")

    def test_signUp_home_page_check_the_title(self):
        signup = SignUp(self.driver)
        title=signup.get_home_page_title()
        assert title == "ProtoCommerce"
        self.driver.get_screenshot_as_file("title_landing page.png")
    def test_signUp_home_page_check_main_menu(self):
        signup = SignUp(self.driver)
        tabs_list=[]
        tabs= signup.get_main_menu_list_main_page()
        for tab in tabs:
            tabs_list.append(tab.text)
        #print(tabs_list)
        expected_list=['Home','Shop']
        #assert 'Home' in tabs_list
        assert expected_list == tabs_list
        self.driver.get_screenshot_as_file("Main_menu_home_page.png")
        self.driver.get_screenshot_as_png()
        self.driver.save_screenshot("ss.png")









