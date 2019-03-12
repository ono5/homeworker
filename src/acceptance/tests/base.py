import socket

from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from acceptance.page_model.base_page import BasePage


class FunctionalTest(StaticLiveServerTestCase):

    # https://stackoverflow.com/questions/44240139/run-liveservertestcase-from-docker-selenium-with-django-1-11
    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(FunctionalTest, cls).setUpClass()

    def setUp(self):
        self.webdriver = webdriver.Remote(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='password123',
            email='admin@example.com'
        )

        self.user = get_user_model().objects.create_user(
            username='user',
            password='password123',
            email='user@example.com'
        )

    def tearDown(self):
        self.webdriver.quit()
