from playwright.sync_api import Page, expect
from page.base_page import BasePage

class LeadsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.button_new_add = self.page.get_by_role('link', name='Add New', exact=True)
        self.first_name_input = self.page.get_by_placeholder('First Name')
        self.last_name_input = self.page.get_by_placeholder('Last Name')
        self.contact_number_input = self.page.get_by_placeholder('Contact Number')
        self.email_input = self.page.get_by_placeholder('Email')
        self.attachment_file_input = self.page.locator("//input[@type='file' and @name='file']")
        self.button_save = self.page.get_by_role('button', name='Save', exact=True)
        self.textbox_search = self.page.get_by_role('searchbox', name='Search', exact=True)
        self.lead_rows = self.page.locator("#xin_table tbody tr")
    # def go_to_lead_page(self, url: str):
    #     """Điều hướng đến trang Leads.

    #     Args:
    #         url (str): URL của trang Leads.
    #     """
    #     self.navigate(url)
       
    def add_new_lead(self, first_name: str, last_name: str, contact_number: str, email: str, path_file: str):
        """Add a new lead with the provided information.    
        Args:
            first_name (str): First name of the lead.
            last_name (str): Last name of the lead.
            contact_number (str): Contact number of the lead.
            email (str): Email address of the lead.
            path_file (str): Path to the attachment file for the lead.
        """
        #Click vào nút "Add New"
        self.click(self.button_new_add) 
        # Nhập trường "First Name"
        self.set_text(self.first_name_input, first_name)
        # Nhập trường "Last Name"
        self.set_text(self.last_name_input, last_name)
        # Nhập trường "Contact Number"
        self.set_text(self.contact_number_input, contact_number )
        # Nhập trường "Email"
        self.set_text(self.email_input, email)
        #Chọn Attachment file
        self.upload_file(self.attachment_file_input, path_file)
        #Click Save button
        self.click(self.button_save)
        
    def verify_added_lead(self, first_name: str, last_name: str, email: str):

        self.set_text(self.textbox_search, email)

        row = self.lead_rows.filter(has_text=email)

        expect(row).to_be_visible()

        expect(row).to_contain_text(first_name)
        expect(row).to_contain_text(last_name)
        expect(row).to_contain_text(email)     
