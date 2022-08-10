from Task.Pages.loginpage import LoginPage
from Tests.basetest import BaseTest
from Configs.configs import Urls


class TestLogin(BaseTest):
    def test_login(self, setup):
        try:
            self.driver = setup
            self.loginPage = LoginPage(self.driver, Urls.KiwiUrl)

            self.loginPage.go_login_page()
            self.loginPage.fill_login_form()
            self.loginPage.login()

            assert Urls.KiwiUrl + 'app/dashboard' == self.driver.current_url

        finally:
            self.driver.close()
