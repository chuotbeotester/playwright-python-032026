from playwright.sync_api import expect
from pages.UI.base_page import BasePage
import time

class LoginBook(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._emailAddress = self.page.get_by_role("textbox", name ="Email address")
        self._passWord = self.page.get_by_role("textbox", name = "Password")
        self._btnLogin = self.page.get_by_role("button", name= "Login account")

    def goto(self,  url: str):
        self._goto(url)
    
    def login(self, usernamre: str, password: str):
        self._fill(self._emailAddress, usernamre)
        self._fill(self._passWord, password)
        self._click(self._btnLogin)
        time.sleep(5)

    