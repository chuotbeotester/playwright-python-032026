from playwright.sync_api import Page
from page.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_component = self.page.locator('//header')
        self.left_menu = self.page.locator('//nav')
        self.label_profile_name = self.page.locator('//a[@href="https://hrm.anhtester.com/erp/my-profile"]//p')
        
    def verify_login_success(self, expected_value: str):
        """Xác minh đăng nhập thành công bằng cách kiểm tra các phần tử giao diện người dùng và tên hồ sơ hiển thị.

        Args:
            expected_value (str): Giá trị tên hồ sơ mong đợi cần xác minh.
        """
        self.verify_element_visible(self.left_menu)
        self.verify_element_visible(self.header_component)
        self.verify_element_text(self.label_profile_name, expected_value, is_exact=False)

    def choose_left_menu(self, main_menu: str, sub_menu: str = None):
        """Điều hướng đến một mục của ứng dụng bằng cách click vào menu chính và menu phụ tùy chọn.

        Args:
            main_menu (str): Tên của menu chính cần click.
            sub_menu (str, optional): Tên của menu phụ cần click (nếu có). Mặc định là None.
        """
        locator_main_menu = self.page.get_by_role("link", name=f" {main_menu}", exact=True)
        self.click(locator_main_menu)
        if sub_menu is not None:
            locator_sub_menu = self.page.get_by_role("link", name=f" {sub_menu}", exact=True)
            self.click(locator_sub_menu)