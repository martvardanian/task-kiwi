import time
from Data.info_convertor import *
from Locators.locators import GenericLocators, ForgotPasswordLocators
from Task.Pages.basepage import BasePage


class RecoverPasswordPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    def go_recover_pass_page(self):
        self.click(GenericLocators.header_sign_in)
        self.click(ForgotPasswordLocators.forgot_password)

    def fill_email(self):
        self.send_keys(ForgotPasswordLocators.email_input, verified_email)
        time.sleep(1)

    def recover_pass(self):
        self.click(ForgotPasswordLocators.recover_password_button)
        time.sleep(1)
