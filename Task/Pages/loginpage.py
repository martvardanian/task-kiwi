import time
from Task.Data.info_convertor import *
from Task.Locators.locators import GenericLocators, LoginLocators
from Task.Pages.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    def go_login_page(self):
        self.click(GenericLocators.header_sign_in)

    def fill_login_form(self):
        self.send_keys(LoginLocators.email_input, verified_email)
        self.send_keys(LoginLocators.password_input, password)
        time.sleep(1)

    def login(self):
        self.click(LoginLocators.login_button)
        time.sleep(1)