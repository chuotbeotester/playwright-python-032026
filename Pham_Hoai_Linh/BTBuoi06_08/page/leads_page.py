from playwright.sync_api import Page
from page.base_page import BasePage

class LeadsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_addNewLead = self.page.get_by_role("link", name= "Add New")
        self.txtbox_firsNameLead = self.page.get_by_role("textbox", name= "First Name")
        self.txtbox_lastNameLead = self.page.get_by_role("textbox", name= "Last Name")
        self.dropdown_genderLead = self.page.locator('//span[@id="select2-gender-p3-container"]')
        self.txtbox_contactNumberLead = self.page.get_by_role("spinbutton", name= "Contact Number")
        self.txtbox_emailLead = self.page.get_by_role("textbox", name= "Email")
        self.uploadFileLead = self.page.get_by_role("button", name= "Choose File")
        self.btn_saveLead = self.page.get_by_role("button", name= "Save")

        self.searchBoxLead = self.page.get_by_role("searchbox", name= "Search")
        self.fullnameTableLead = self.page.locator('//h6[@class="m-b-0"]')
        self.emailTableLead = self.page.locator('//p[@class="m-b-0"]')
        self.contacNumberTableLead = self.page.locator('//tr[@class="odd"]/td[2]')
        self.genderTableLead = self.page.locator('//tr[@class="odd"]/td[3]')

        def go_to_lead_page(self):
            self.navigate_to("https://hrm.anhtester.com/erp/leads-list")

        def add_a_new_lead (self, firstName, lastName, gender, contactNumber, email, pathfile):
            self.set_text(firstName)
            self.set_text(lastName)
            self.select_dropdown(gender)
            self.set_text(contactNumber)
            self.set_text(email)
            self.uploadFileLead(pathfile)
            self.click(self.btn_saveLead)

        def verify_added_client(self, firstName: str, lastName: str, contactNumber: int, gender, email: str):
            self.set_text(self.searchBoxLead, email)
            self.verify_element_text(self.fullnameTableLead, firstName+" "+lastName)
            self.verify_element_text(self.emailTableLead, email)
            self.verify_element_text(self.contacNumberTableLead, contactNumber)
            self.verify_element_text(self.genderTableLead, gender)