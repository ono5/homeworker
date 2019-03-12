from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """Login Page"""
    LOGIN_ID = (By.ID, 'id_username')
    LOGIN_PASSWORD = (By.ID, 'id_password')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Login"]')
    ERROR_MESSAGE = (By.ID, 'id_error')
