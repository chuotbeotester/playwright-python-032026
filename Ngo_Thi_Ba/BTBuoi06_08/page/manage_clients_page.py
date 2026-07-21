from playwright.sync_api import Page, expect
from page.base_page import BasePage
from utils.path_helper import PathFile


class ManageClientsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        #Click vào nút "Add Client"
        self.add_client_button = page.get_by_role("link", name="Add New")
        #Field First Name
        self.client_firstname_input = page.get_by_role("textbox", name="First Name")
        #Field Last Name
        self.client_lastname_input = page.get_by_role("textbox", name="Last Name")
        #Field Password
        self.client_password_input = page.get_by_role("textbox", name="Password")
        #Field Contact Number
        self.client_contact_number_input = page.locator('//input[@name="contact_number"]')
        #Field Email
        self.client_email_input = page.get_by_role("textbox", name="Email")
        #Field Username
        self.client_username_input = page.get_by_role("textbox", name="Username")
        #Field Attachment
        self.client_attachment_input = page.locator('input[type="file"][name="file"]')
        #Save button    
        self.save_button = page.get_by_role("button", name="Save")
        #Search input
        self.search_input = page.get_by_role("searchbox", name="Search")
        
    def go_to_manage_clients_page(self):
        """Điều hướng đến trang quản lý khách hàng.
        """
        self.navigate("https://hrm.anhtester.com/erp/clients-list")
    

    def add_new_client(self, first_name: str, last_name: str, password: str, email: str, contact_number: str, username: str, attachment):
        """Add a new client 
        Args:
            first_name (str): First name of the client.
            last_name (str): Last name of the client.
            password (str): Password for the client.
            email (str): Email address of the client.
            contact_number (str): Contact number of the client.
            username (str): Username for the client.
            attachment (str): Path to the attachment file for the client.
        """
        
        #Click vào nút "Add Client"
        self.add_client_button.click()
        # Nhập trường "First Name"
        self.client_firstname_input.fill(first_name)
        # Nhập trường "Last Name"
        self.client_lastname_input.fill(last_name)
        # Nhập trường "Password"
        self.client_password_input.fill(password)
        # Nhập trường "Email"
        self.client_email_input.fill(email)
        # Nhập trường "Contact Number"
        self.client_contact_number_input.fill(contact_number)
        # Nhập trường "Username"
        self.client_username_input.fill(username)
        # Chọn "Attachment"
        self.upload_file(self.client_attachment_input, PathFile.get_string_file_path(attachment))
        # Click nút Save
        self.save_button.click()

    
    def verify_added_client(self, email: str):
        """Verify that the added client is present in the list of clients.

        Args:
            first_name (str): First name of the client.
            last_name (str): Last name of the client.
            email (str): Email address of the client.
        """
        # Nhập tên khách hàng vào ô tìm kiếm
        self.set_text(self.search_input, email)
        # Kiểm tra xem khách hàng vừa thêm có xuất hiện trong danh sách hay không
        # expect(self.page.get_by_text(first_name)).to_be_visible()
        # expect(self.page.get_by_text(username, exact = True)).to_be_visible()
        expect(self.page.get_by_text(email)).to_be_visible()