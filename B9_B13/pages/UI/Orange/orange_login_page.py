from playwright.sync_api import expect
from ..base_page import BasePage
from .linked_page import Linked

import time

class LoginOrange(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.linked_url = self.page.locator("//a[contains(@href,'linkedin')]")
        self.btnLogin = self.page.get_by_role("button", name= "Login")

    def navigate_to_orange_page(self):
        self._goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    

    def click_open_linked_page(self):
        new_page = self._click_open_new_tab(self.linked_url)
        return Linked(new_page)

    def login(self):
        self._click(self.btnLogin)
     
