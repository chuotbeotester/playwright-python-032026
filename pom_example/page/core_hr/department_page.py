from playwright.sync_api import Page, expect
from page.base_page import BasePage
from page.home_page import HomePage

class DepartmentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_name = "Department"
        self.home_page = HomePage(page)
        self.textbox_name = self.page.get_by_role("textbox", name="Name", exact=True)
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)
        

    def go_to_department_page(self):
        """Điều hướng tới trang Department."""
        department_header = self.page.locator(f'//div[@class="page-header"]//li[normalize-space()="{self.page_name}"]')
        tab_department = self.page.locator(f'//li[contains(.,"{self.page_name}")][contains(@class,"nav-item")]')
        self.home_page.choose_left_menu("Core HR", self.page_name)
        self.verify_element_visible(department_header)
        expect(tab_department).to_contain_class("active")

    def create_department(self, department_name: str):
        """Tạo một Department mới với tên được chỉ định.

        Args:
            department_name (str): Tên Department cần tạo.
        """
        self.set_text(self.textbox_name, department_name)
        self.click(self.button_save)
        
    def verify_create_success(self, expected_value: str):
        """Xác minh tạo Department thành công bằng cách tìm kiếm và kiểm tra dữ liệu trong bảng.

        Args:
            expected_value (str): Tên Department mong đợi hiển thị trong bảng để xác minh.
        """
        self.set_text(self.textbox_search, expected_value)
        cell_department_name = self.page.locator('//table[@id="xin_table"]//tr[1]/td[1]')
        self.verify_element_text(cell_department_name, expected_value, is_exact=False)