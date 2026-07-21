from playwright.sync_api import expect
from ..base_page import BasePage
from ..home_page import HomePage
import time

class Project(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.project_menu = self.page.get_by_role("link", name = "Projects")
        self.btn_Addnew = self.page.get_by_role("link", name = "Add New")

    def open_project_page(self):
        self._click(self.project_menu)

    def open_add_new_popup(self):
        self._click(self.btn_Addnew)
        time.sleep(2)


    