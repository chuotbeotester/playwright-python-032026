from page.base_page import BasePage
from utils.path_helper import PathFile
from utils.random_data_helper import FakeData

class ManageClientPage(BasePage):
    client_data = PathFile.read_json_data("input_data/client_data.json")
    def __init__(self, page):
        super().__init__(page)
        self.manage_client = self.page.locator("//ul[@class='breadcrumb']/li[normalize-space()='Manage Clients']")
        self.button_add_new = self.page.get_by_role("link", name="Add New")
        self.textbox_first_name = self.page.get_by_role("textbox", name="First Name")
        self.textbox_last_name = self. page.get_by_role("textbox", name="Last Name")
        self. textbox_pwd = page.get_by_role("textbox", name="Password")
        self.textbox_contact_number = self.page.locator("//label[@for='contact_number']/following-sibling::input")
        self.select_gender = self.page.locator("//label[contains(text(), 'Gender')]/following-sibling::select")
        self.textbox_email = self.page.get_by_role("textbox", name="Email")
        self.textbox_username = self.page.get_by_role("textbox", name="Username")
        self.open_path_file = self.page.get_by_role("button", name="Choose File")
        self.button_save = page.get_by_role("button", name="Save")
        self.button_reset = self.page.get_by_role("button", name="Reset")
        self.textbox_search = self.page.get_by_role("searchbox", name="Search")
        
        
    def create_new_client(self):       
        """
        Tạo mới một Client bằng cách điền đầy đủ thông tin vào form Add Client.

        Hàm sẽ thực hiện các bước sau:
            1. Mở form Add New Client.
            2. Điền các trường nhập liệu bắt buộc.
            3. Chọn giới tính từ danh sách dropdown.
            4. Upload hình ảnh được chỉ định.
            5. Nhấn nút Save để tạo Client.

        Args:

        """       
     
        file_name = self.client_data["FILE_NAME"]
        client = FakeData.create_client()  
        input_fields = {
            self.textbox_first_name: client["first_name"],
            self.textbox_last_name: client["last_name"],
            self.textbox_pwd: client["pwd"],
            self.textbox_contact_number: client["contact_number"],
            self.textbox_email: client["email"],
            self.textbox_username: client["usr"],
        }

        #Click Add New button
        self.click(self.button_add_new)

        #Fill in informations to create the client
        for locator, value in input_fields.items():
            self.set_text(locator, value)

        #Select the gender
        self.select_dropdown(self.select_gender, client["gender"], True)
        
        #Upload file
        self.upload_file(self.open_path_file, file_name)
        
        #Click Save button
        self.click(self.button_save)

        return client


    def verify_toast_message(self, expected_message: str):
        """
        Verify the toast notification message.

        Args:
            expected_message (str): Expected toast message.
        """

        toast_message = self.page.locator("//div[contains(@class,'toast-message')]")
        self.verify_element_visible(toast_message)
        self.verify_element_text(toast_message, expected_message)
        
        
    def verify_created_client_details(self, client : dict):
        """
        Verify client được tạo thành công bằng cách search client vừa tạo và kiểm tra dữ liệu hiển thị ở dòng đầu tiên của bảng.

        Args:
            client (dict): Generated client data returned by FakeData.create_client().
        """
        full_name = f"{client['first_name']} {client['last_name']}"
        status = self.client_data["CLIENT_STATUS"]
        first_row = "//table[@id='xin_table']/tbody/tr[1]"
        expected_data = {
            f"{first_row}/td[1]//h6": full_name,
            f"{first_row}/td[1]//p": client['email'],
            f"{first_row}/td[2]": client['usr'],
            f"{first_row}/td[3]": client['contact_number'],
            f"{first_row}/td[4]": client['gender'],
            f"{first_row}/td[6]": status
        }

        #Search the created client
        self.set_text(self.textbox_search, full_name)
        
        #Verify the created client detail
        for locator, expected_text in expected_data.items():
            self.verify_element_text(self.page.locator(locator), expected_text, is_exact=False)