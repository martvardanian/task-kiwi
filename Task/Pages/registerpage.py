import time
from Data.info_convertor import *
from Locators.locators import GenericLocators, RegisterLocators
from Task.Pages.basepage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    def go_register_page(self):
        self.click(GenericLocators.header_sign_in)
        self.click(RegisterLocators.next_sign_up)

    def fill_registration_form(self):
        self.send_keys(RegisterLocators.email_input, new_email)
        self.send_keys(RegisterLocators.password_input, password)
        time.sleep(1)

    def register(self):
        self.click(RegisterLocators.register_sign_up)
        time.sleep(1)