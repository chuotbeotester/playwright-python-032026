from playwright.sync_api import Page
from page.base_page import BasePage
from utils.path_helper import PathFile
from utils.client import Client


class ManageClientsPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/clients-list"
    # Ảnh đại diện (Profile Picture) là trường BẮT BUỘC của form Add Client.
    PROFILE_PICTURE = "upload_files/test_client.jpeg"

    def __init__(self, page: Page):
        super().__init__(page)
        self.link_add_new = self.page.get_by_role("link", name="Add New", exact=True)
        self.add_form = self.page.locator("#add_form")
        self.textbox_first_name = self.add_form.get_by_placeholder("First Name", exact=True)
        self.textbox_last_name = self.add_form.get_by_placeholder("Last Name", exact=True)
        self.textbox_password = self.add_form.get_by_placeholder("Password", exact=True)
        self.textbox_contact_number = self.add_form.get_by_placeholder("Contact Number", exact=True)
        self.textbox_email = self.add_form.get_by_placeholder("Email", exact=True)
        self.textbox_username = self.add_form.get_by_placeholder("Username", exact=True)
        self.input_profile_picture = self.add_form.locator('input[type="file"][name="file"]')
        self.button_save = self.add_form.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)
        self.button_delete_first_row = self.page.locator(
            '//table[@id="xin_table"]//tbody/tr[1]//button[contains(@class,"delete")]'
        )
        self.delete_modal = self.page.locator(".delete-modal")
        self.button_confirm_delete = self.delete_modal.get_by_role("button", name="Confirm", exact=True)
        # Client vừa tạo — dùng để dọn dữ liệu sau khi test xong.
        self.created_client = None

    def go_to_manage_clients_page(self):
        """Truy cập trang Manage Clients và xác minh trang đã sẵn sàng."""
        self.navigate(self.URL)
        self.verify_element_visible(self.link_add_new)

    def create_client(self, client: Client):
        """Tạo một Client mới: mở form Add New, nhập các trường bắt buộc và lưu.

        Args:
            client (Client): Bộ dữ liệu Client cần tạo.
        """
        self.click(self.link_add_new)
        self.verify_element_visible(self.textbox_first_name)
        self.set_text(self.textbox_first_name, client.first_name)
        self.set_text(self.textbox_last_name, client.last_name)
        self.set_text(self.textbox_password, client.password)
        self.set_text(self.textbox_contact_number, client.contact_number)
        self.set_text(self.textbox_email, client.email)
        self.set_text(self.textbox_username, client.username)
        # Profile Picture bắt buộc — thiếu sẽ bị lỗi "The profile picture field is required."
        self.upload_file(self.input_profile_picture, PathFile.get_string_file_path(self.PROFILE_PICTURE))
        self.click(self.button_save)
        # Ghi nhận để dọn dữ liệu test sau khi chạy xong.
        self.created_client = client

    def verify_create_success(self, client: Client):
        """Xác minh tạo Client thành công bằng cách tìm kiếm trong bảng "List All Clients".

        Args:
            client (Client): Client vừa tạo, dùng first_name để tìm kiếm và đối chiếu.
        """
        self.set_text(self.textbox_search, client.first_name)
        cell_client_name = self.page.locator('//table[@id="xin_table"]//tbody/tr[1]/td[1]')
        self.verify_element_text(cell_client_name, client.first_name, is_exact=False)

    def delete_client(self, client: Client = None):
        """Xóa một Client rồi xác nhận. Dùng cho teardown để dọn dữ liệu test.

        Args:
            client (Client, optional): Client cần xóa. Mặc định None → xóa Client vừa tạo
                (self.created_client). Không làm fail test nếu xóa lỗi.
        """
        client = client or self.created_client
        if client is None:
            return
        self.navigate(self.URL)
        try:
            self.set_text(self.textbox_search, client.first_name)
            self.click(self.button_delete_first_row)
            self.verify_element_visible(self.button_confirm_delete)
            self.click(self.button_confirm_delete)
        except Exception as error:
            print(f"[cleanup] Không xóa được client '{client.first_name}': {error}")
        finally:
            self.created_client = None
