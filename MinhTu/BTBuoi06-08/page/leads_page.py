from playwright.sync_api import expect
from page.base_page import BasePage
from utils.path_helper import PathFile
from utils.random_data_helper import FakeData
import time

class LeadsPage(BasePage):
    lead_data = PathFile.read_json_data("input_data/client_data.json")
    def __init__(self, page):
        super().__init__(page)
        self.manage_Lead = self.page.locator("//ul[@class='breadcrumb']/li[normalize-space()='Leads']")
        self.button_add_new = self.page.get_by_role("link", name="Add New")
        self.textbox_first_name = self.page.get_by_role("textbox", name="First Name")
        self.textbox_last_name = self. page.get_by_role("textbox", name="Last Name")
        self.textbox_contact_number = self.page.locator("//label[@for='contact_number']/following-sibling::input")
        self.select_gender = self.page.locator("//label[contains(text(), 'Gender')]/following-sibling::select")
        self.textbox_email = self.page.get_by_role("textbox", name="Email")
        self.open_path_file = self.page.get_by_role("button", name="Choose File")
        self.button_save = page.get_by_role("button", name="Save")
        self.button_reset = self.page.get_by_role("button", name="Reset")
        self.textbox_search = self.page.get_by_role("searchbox", name="Search")
        
        
    def create_new_lead(self):       
        """
        Tạo mới một Lead bằng cách điền đầy đủ thông tin vào form Add New Lead.

        Hàm sẽ thực hiện các bước sau:
            1. Mở form Add New Lead.
            2. Điền các trường nhập liệu bắt buộc.
            3. Chọn giới tính từ danh sách dropdown.
            4. Upload hình ảnh được chỉ định.
            5. Nhấn nút Save để tạo Lead.

        Args:

        """       
     
        file_name = self.lead_data["FILE_NAME"]
        Lead = FakeData.create_lead()  
        input_fields = {
            self.textbox_first_name: Lead["first_name"],
            self.textbox_last_name: Lead["last_name"],
            self.textbox_contact_number: Lead["contact_number"],
            self.textbox_email: Lead["email"]
        }

        #Click Add New button
        self.click(self.button_add_new)

        #Fill in informations to create the Lead
        for locator, value in input_fields.items():
            self.set_text(locator, value)

        #Select the gender
        self.select_dropdown(self.select_gender, Lead["gender"], True)
        
        #Upload file
        self.upload_file(self.open_path_file, file_name)
        
        #Click Save button
        self.click(self.button_save)

        return Lead


    def verify_toast_message(self, expected_message: str):
        """
        Verify the toast notification message.

        Args:
            expected_message (str): Expected toast message.
        """

        toast_message = self.page.locator("//div[contains(@class,'toast-message')]")
        self.verify_element_visible(toast_message)
        self.verify_element_text(toast_message, expected_message)
        
        
    def verify_created_lead_details(self, Lead : dict):
        """
        Verify Lead được tạo thành công bằng cách search Lead vừa tạo và kiểm tra dữ liệu hiển thị ở dòng đầu tiên của bảng.

        Args:
            Lead (dict): Generated lead data returned by FakeData.create_lead().
        """
        full_name = f"{Lead['first_name']} {Lead['last_name']}"
        status = self.lead_data["LEAD_STATUS"]
        first_row = "//table[@id='xin_table']/tbody/tr[1]"
        expected_data = {
            f"{first_row}/td[1]//h6": full_name,
            f"{first_row}/td[1]//p": Lead['email'],
            f"{first_row}/td[2]": Lead['contact_number'],
            f"{first_row}/td[3]": Lead['gender'],
            f"{first_row}/td[5]": status
        }

        #Search the created Lead
        self.set_text(self.textbox_search, full_name)
        
        #Verify the created Lead detail
        for locator, expected_text in expected_data.items():
            self.verify_element_text(self.page.locator(locator), expected_text, is_exact=False)