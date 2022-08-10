from Locators.locators import ForgotPasswordLocators
from Task.Pages.basepage import BasePage
from Task.Pages.recoverpasswordpage import RecoverPasswordPage
from Tests.basetest import BaseTest
from Configs.configs import Urls


class TestRecoverPass(BaseTest):
    def test_recover_pass(self, setup):
        try:
            self.driver = setup
            self.recoverpassPage = RecoverPasswordPage(self.driver, Urls.KiwiUrl)
            self.basePage = BasePage(self.driver)

            self.recoverpassPage.go_recover_pass_page()
            self.recoverpassPage.fill_email()
            self.recoverpassPage.recover_pass()
            success_message = self.basePage.get_text(ForgotPasswordLocators.confirm_recover_pass_pop_up)
            assert 'Check your email' == success_message

        finally:
            self.driver.close()
