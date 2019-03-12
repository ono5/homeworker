from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

from acceptance.locators.base_page import BasePageLocators


class BasePage(object):
    """Base Page"""

    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.num = 1

    @property
    def url(self):
        """get url"""
        return ""

    @property
    def body(self):
        """get body tag"""
        return self.webdriver.find_element(*BasePageLocators.BODY)
