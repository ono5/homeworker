from acceptance.common.common import *
from acceptance.page_model.login_page import LoginPage
from acceptance.tests.base import FunctionalTest

S_SUB_FOLDER_PATH = 'screen_shot/login_page'
L_SUB_FOLDER_PATH = 'logs/login_page'
L_FILE_NAME = 'login_page.log'

ADMIN_USER = 'admin'
ADMIN_PASSWORD = 'password123'

USER = 'user'
USER_PASSWORD = 'password123'


class LoginPageTest(FunctionalTest):
    def set_up(self):
        self.page = LoginPage(self.webdriver)
        self.live_server_url = self.live_server_url

    def test_case_1(self):
        """Success Login by admin user"""
        self.set_up()

        open_page(self.live_server_url, self.page)
        get_screen_shot(f'Test-Case-1-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        input_text_box(self.page.login_id, ADMIN_USER)
        input_text_box(self.page.login_password, ADMIN_PASSWORD)
        get_screen_shot(f'Test-Case-1-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        click_button(self.page.login_button)
        get_screen_shot(f'Test-Case-1-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        assert self.page.webdriver.title == 'Dashboard'

    def test_case_2(self):
        """Success Login by user"""
        self.set_up()

        open_page(self.live_server_url, self.page)
        get_screen_shot(f'Test-Case-2-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        input_text_box(self.page.login_id, USER)
        input_text_box(self.page.login_password, USER_PASSWORD)
        get_screen_shot(f'Test-Case-2-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        click_button(self.page.login_button)
        get_screen_shot(f'Test-Case-2-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        assert self.page.webdriver.title == 'Dashboard'


    def test_case_3(self):
        """False Login by user"""
        self.set_up()

        open_page(self.live_server_url, self.page)
        get_screen_shot(f'Test-Case-3-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        input_text_box(self.page.login_id, 'hoge')
        input_text_box(self.page.login_password, 'hoge')
        get_screen_shot(f'Test-Case-3-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        click_button(self.page.login_button)
        get_screen_shot(f'Test-Case-3-{self.page.num}', self.page, S_SUB_FOLDER_PATH)

        assert self.page.get_error_message.text == "Your username and password didn't match. Please try again."
        assert self.page.webdriver.title == 'Log-in'