from playwright.sync_api import Page
from page.login_page import LoginPage

def test_login(page: Page):
    URL = 'https://hrm.anhtester.com/'
    USERNAME = 'admin_example'
    PASSWORD = '123456'
    
    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)