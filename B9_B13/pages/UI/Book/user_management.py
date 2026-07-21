from playwright.sync_api import expect
from pages.UI.base_page import BasePage
import time

class UserManagement(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.searchbox = self.page.get_by_role("textbox", name ="Search user (name, email, phone or address)")
        self.kebab_menu = self.page.locator("//tbody//button[contains(@class, 'MuiIconButton')]")
        self.btn_Edit = self.page.get_by_role("menuitem", name = "Edit")
        self.heading = self.page.get_by_role("heading", name = "Update user")

    def goto(self):
        self._goto("https://book.anhtester.com/user-management")
    
    def search_username(self, text: str):
        self._fill(self.searchbox, text)
        time.sleep(3)
    
    def edit_user(self):
        self._click(self.kebab_menu)
        self._click(self.btn_Edit)
        self._assert_visible(self.heading)
    
    def verify_edit_button_disable(self):
        self._click(self.kebab_menu)
        self._click(self.btn_Edit)
        self._assert_disable(self.btn_Edit)

    