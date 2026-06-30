from playwright.sync_api import Page
from page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_component = self.page.get_by_role("banner")
        self.left_menu = self.page.get_by_role("navigation")
        self.label_profile_name = self.page.locator('a[href="https://hrm.anhtester.com/erp/my-profile"] p')

    def choose_left_menu(self, main_menu: str, sub_menu: str = None):
        """Nhấn main menu; nếu truyền sub_menu thì tiếp tục nhấn vào mục con."""
        self.click(self.page.get_by_role("link", name=f" {main_menu}", exact=True))
        if sub_menu is not None:
            self.click(self.page.get_by_role("link", name=f" {sub_menu}", exact=True))
