from playwright.sync_api import Page, expect
from page.base_page import BasePage
from page.home_page import HomePage


class DesignationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_name = "Designation"
        self.home_page = HomePage(page)
        self.dropdown_department = self.page.locator('//div[@id="department_ajax"]//select')
        self.textbox_designation_name = self.page.get_by_role("textbox", name="Designation Name", exact=True)
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)

    def go_to_designation_page(self):
        """Điều hướng đến trang và xác nhận landing qua breadcrumb hiển thị và tab đang active."""
        designation_header = self.page.locator(f'//div[@class="page-header"]//li[normalize-space()="{self.page_name}"]')
        tab_designation = self.page.locator(f'//li[contains(.,"{self.page_name}")][contains(@class,"nav-item")]')
        self.home_page.choose_left_menu("Core HR", self.page_name)
        self.verify_element_visible(designation_header)
        expect(tab_designation).to_contain_class("active")

    def create_designation(self, department_name: str, designation_name: str):
        self.select_dropdown(self.dropdown_department, department_name, by_label=True)
        self.set_text(self.textbox_designation_name, designation_name)
        self.click(self.button_save)

    def verify_create_success(self, department_name: str, designation_name: str):
        """Tìm kiếm theo tên designation rồi kiểm tra cả tên designation lẫn department ở dòng đầu bảng."""
        self.set_text(self.textbox_search, designation_name)
        cell_designation_name = self.page.locator('//table[@id="xin_table"]//tr[1]/td[1]')
        cell_department_name = self.page.locator('//table[@id="xin_table"]//tr[1]/td[2]')
        self.verify_element_text(cell_designation_name, designation_name, is_exact=False)
        self.verify_element_text(cell_department_name, department_name, is_exact=False)
