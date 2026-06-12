from playwright.sync_api import Page, expect
from page.base_page import BasePage
from page.home_page import HomePage

class PoliciesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_name = "Policies"
        self.home_page = HomePage(page)
        self.textbox_policy_title = self.page.get_by_role("textbox", name="Title", exact=True)
        self.textbox_policy_description = self.page.get_by_role("textbox", name="Description", exact=True)
        self.input_file_attachment = self.page.locator('//form[@name="add_policy"]//input[@type="file"]')
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)        

    def go_to_policies_page(self):
        """Điều hướng tới trang page Policies"""
        policies_header = self.page.locator(f'//div[@class="page-header"]//li[normalize-space()="{self.page_name}"]')
        tab_policies = self.page.locator(f'//li[contains(.,"{self.page_name}")][contains(@class,"nav-item")]')
        self.home_page.choose_left_menu("Core HR", self.page_name)
        self.verify_element_visible(policies_header)
        expect(tab_policies).to_contain_class("active")

    def create_policies(self, policy_name: str, policy_description: str, file_path: str):
        """Tạo một Policies mới với tiêu đề, mô tả và tệp đính kèm được chỉ định.

        Args:
            policy_name (str): Tên/Tiêu đề của Policies cần tạo.
            policy_description (str): Mô tả chi tiết của Policies.
            file_path (str): Đường dẫn tuyệt đối của tệp tin đính kèm cần tải lên.
        """
        self.set_text(self.textbox_policy_title, policy_name)
        self.set_text(self.textbox_policy_description, policy_description)
        self.upload_file(self.input_file_attachment, file_path)
        self.click(self.button_save)
        
    def verify_create_success(self, expected_text: str):
        """Xác minh tạo Policies thành công bằng cách tìm kiếm và kiểm tra tiêu đề trong bảng.

        Args:
            expected_text (str): Tiêu đề Policies mong đợi dùng để tìm kiếm và kiểm tra trong bảng.
        """
        self.set_text(self.textbox_search, expected_text)
        cell_policy_name = self.page.locator('//table[@id="xin_table"]//tr[1]/td[1]//h6')
        self.verify_element_text(cell_policy_name, expected_text, is_exact=False)