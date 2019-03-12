from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """Base Locator"""
    BODY = (By.TAG_NAME, 'body')
    