from Locators.locators import RegisterLocators
from Task.Pages.basepage import BasePage
from Task.Pages.registerpage import RegisterPage
from Tests.basetest import BaseTest
from Configs.configs import Urls


class TestRegister(BaseTest):
    def test_register(self, setup):
        try:
            self.driver = setup
            self.registerPage = RegisterPage(self.driver, Urls.KiwiUrl)
            self.basePage = BasePage(self.driver)

            self.registerPage.go_register_page()
            self.registerPage.fill_registration_form()
            self.registerPage.register()
            success_message = self.basePage.get_text(RegisterLocators.confirm_reg_pop_up)
            assert 'Sign Up success' == success_message

        finally:
            self.driver.close()
