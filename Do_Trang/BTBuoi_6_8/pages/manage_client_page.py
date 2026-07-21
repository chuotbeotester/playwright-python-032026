from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.path_helper import PathFile
from models.client import Client


class ManageClientsPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/clients-list"

    def __init__(self, page: Page):
        super().__init__(page)
        self.text_list_all_clients = self.page.get_by_role("heading", name="List All Clients")
        self.link_add_new = self.page.get_by_role("link", name="Add New", exact=True)
        
        self.textbox_first_name = self.page.get_by_role("textbox", name="First Name")
        self.textbox_last_name = self.page.get_by_role("textbox", name="Last Name")
        self.textbox_password = self.page.get_by_role("textbox", name="Password")
        self.textbox_contact_number = self.page.locator('//input[@name="contact_number"]')
        self.textbox_email = self.page.get_by_role("textbox", name="Email")
        self.textbox_username = self.page.get_by_role("textbox", name="Username")
        self.cbb_gender = self.page.locator("//select[@name='gender']")
        self.input_profile_picture = self.page.get_by_role("button", name="Choose File")

        self.button_save = self.page.get_by_role("button", name="Save")

        self.textbox_search = self.page.get_by_role("searchbox", name="Search")
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
        self.verify_element_visible(self.text_list_all_clients)

    def create_client(self, client: Client):
        """Tạo một Client mới: 
        Args:
            client (Client): Client cần tạo
        """
        # CLick btn Add New
        self.click(self.link_add_new)
        # First Name
        self.set_text(self.textbox_first_name, client.first_name)
        # Last Name
        self.set_text(self.textbox_last_name, client.last_name)
        # Password
        self.set_text(self.textbox_password, client.password)
        # Contact Number
        self.set_text(self.textbox_contact_number, client.contact_number)
        # Email
        self.set_text(self.textbox_email, client.email)
        # Username
        self.set_text(self.textbox_username, client.username)
        # Droplist Gender
        self.select_dropdown(self.cbb_gender, client.gender, True)
        # Upload file vào trường Attachment
        self.upload_file(self.input_profile_picture, PathFile.get_string_file_path(client.profile_picture))
        
        # 4. Click btn Save
        self.click(self.button_save)
        self.created_client = client

    def verify_create_manage_client_success(self, client: Client):
        """Verify Client tạo thành công bằng cách tìm kiếm trong bảng "List All Clients" với giá trị email vừa đc tạo.

        Args:
            client (Client): Client vừa tạo, dùng email để tìm kiếm và đối chiếu.
        """
        self.set_text(self.textbox_search, client.email)
        first_row = self.page.locator("//table[@id='xin_table']//tbody/tr")
        self.verify_element_text(first_row.locator("xpath=.//h6"), f"{client.first_name} {client.last_name}", is_exact=False)
        self.verify_element_text(first_row.locator("xpath=.//p"), client.email, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[2]"), client.username, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[3]"), client.contact_number, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[4]"), client.gender, is_exact=False)

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
            self.set_text(self.textbox_search, client.email)
            self.click(self.button_delete_first_row)
            self.verify_element_visible(self.button_confirm_delete)
            self.click(self.button_confirm_delete)
        except Exception as error:
            print(f"Không xóa được client với email'{client.email}': {error}")
        finally:
            self.created_client = None