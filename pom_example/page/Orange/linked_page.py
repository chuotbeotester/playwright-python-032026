from playwright.sync_api import expect
from ..base_page import BasePage
import re

class Linked(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def assert_is_linked_page(self):
        expect(self.page).to_have_url(re.compile("linkedin.com/company/orangehrm"))
    