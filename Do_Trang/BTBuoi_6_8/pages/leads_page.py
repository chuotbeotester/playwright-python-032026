from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.path_helper import PathFile
from models.lead import Lead

class LeadPage(BasePage):
    URL_leads = "https://hrm.anhtester.com/erp/leads-list"

    def __init__(self, page: Page):
        super().__init__(page)
        self.text_list_all_leads = self.page.get_by_role("heading", name="List All Leads")
        
        self.link_add_new = self.page.get_by_role("link", name="Add New", exact=True)

        self.textbox_first_name = self.page.get_by_role("textbox", name="First Name")
        self.textbox_last_name = self.page.get_by_role("textbox", name="Last Name")
        self.textbox_contact_number = self.page.locator('//input[@name="contact_number"]')
        self.textbox_email = self.page.get_by_role("textbox", name="Email")
        self.cbb_gender = self.page.locator("//select[@name='gender']")
        self.input_profile_picture = self.page.get_by_role("button", name="Choose File")

        self.button_save = self.page.get_by_role("button", name="Save")
        self.textbox_search = self.page.get_by_role("searchbox", name="Search")

    def go_to_lead_page(self):
        """Truy cập trang Leads và xác minh trang đã sẵn sàng."""
        self.navigate(self.URL_leads)
        self.verify_element_visible(self.text_list_all_leads)

    def create_leads(self, lead: Lead):
        """Tạo một Lead mới: 
        Args:
            lead (Lead): Lead cần tạo
        """
        # CLick btn Add New
        self.click(self.link_add_new)
        # First Name
        self.set_text(self.textbox_first_name, lead.first_name)
        # Last Name
        self.set_text(self.textbox_last_name, lead.last_name)
        # Contact Number
        self.set_text(self.textbox_contact_number, lead.contact_number)
        # Email
        self.set_text(self.textbox_email, lead.email)
        # Droplist Gender
        self.select_dropdown(self.cbb_gender, lead.gender, True)
        # Upload file vào trường Attachment
        self.upload_file(self.input_profile_picture, PathFile.get_string_file_path(lead.profile_picture))
        
        # 4. Click btn Save
        self.click(self.button_save)

    def verify_create_leads_success(self, lead: Lead):
        """Verify Lead tạo thành công bằng cách tìm kiếm trong bảng "List All Leads" với giá trị email vừa đc tạo.

        Args:
            lead (Lead): Lead vừa tạo, dùng email để tìm kiếm và đối chiếu.
        """
        self.set_text(self.textbox_search, lead.email)
        first_row = self.page.locator("//table[@id='xin_table']//tbody/tr")
        self.verify_element_text(first_row.locator("xpath=.//h6"), f"{lead.first_name} {lead.last_name}", is_exact=False)
        self.verify_element_text(first_row.locator("xpath=.//p"), lead.email, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[2]"), lead.contact_number, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[3]"), lead.gender, is_exact=False)
        self.verify_element_text(first_row.locator("xpath=./td[5]"), "Lead", is_exact=False)