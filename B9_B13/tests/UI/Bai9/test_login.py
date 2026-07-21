from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect
import time


def test_login_success(page):
    login = LoginPage(page)
    login.goto("https://hrm.anhtester.com/erp/clients-list")
