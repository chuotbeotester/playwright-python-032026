from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect
import time


def test_verrify_add_new_page(loggedin_home_storage):
    loggedin_home_storage.navigate_to_home()
    loggedin_home_storage.navigate_to_my_account()

