from playwright.sync_api import expect
from .base_page import BasePage
from component.header_component import HeaderComponent
import time

class HomePage(BasePage, HeaderComponent):
    def __init__(self, page):
        super().__init__(page)
        self.logo = self.page.locator("//header//*[contains(@class, 'logo')]")
        self.profile = self.page.locator("//div//li//span[normalize-space()='Admin Example']")
        self.myAccount = self.page.locator("//a//span[normalize-space()='My Account']")

    def navigate_to_home(self):
        self._goto("https://hrm.anhtester.com/erp/desk")   

    def navigate_to_my_account(self):
        self._click(self.profile)
        self._click(self.myAccount)
        time.sleep(3)
