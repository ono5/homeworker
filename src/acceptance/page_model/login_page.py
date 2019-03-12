from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from acceptance.locators.login_page import LoginPageLocators
from acceptance.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        """Get URL of login page"""
        return super(LoginPage, self).url + '/login'

    @property
    def login_id(self):
        """Login ID 取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_ID)

    @property
    def login_password(self):
        """ Password 取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_PASSWORD)

    @property
    def login_button(self):
        """ Login ボタン取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def get_error_message(self):
        """Get Error Page"""
        return WebDriverWait(self.webdriver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE))
