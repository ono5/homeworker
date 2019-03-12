import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from pathlib import Path

HOME_DIR = str(Path.home())

# setting param
######################################################
# example ; C:\\Users\\hoge\\pravas_auto_test\\evidence'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, 'evidence/')
#######################################################


def get_screen_shot(description, page, sub_folder) ->None:
    """Get Screen shot"""

    full_log_path = LOG_PATH + sub_folder
    if os.path.isdir(full_log_path):
        pass
    else:
        os.mkdir(full_log_path)

    if hasattr(page, 'num'):
        page.num += 1

    page.webdriver.get_screenshot_as_file(f'{full_log_path}/{description}.png')
    return


def open_page(live_server_url, page) -> None:
    """open web browser with 100% width """
    page.webdriver.get(live_server_url + page.url)
    page.body.send_keys(Keys.CONTROL + '0')
    page.webdriver.maximize_window()

    return


def input_text_box(elem, content) -> None:
    """Submit string text into textbox"""
    elem.clear()
    elem.send_keys(content)
    return


def click_button(elem) -> None:
    """click button"""
    elem.click()
    return


def login(page: object, login_id: str, login_password: str) -> None:
    """login from login page to top page"""
    input_text_box(page.login_id, login_id)
    input_text_box(page.login_password, login_password)
    click_button(page.login_button)
    return

