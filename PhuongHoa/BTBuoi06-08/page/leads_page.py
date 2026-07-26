from page.base_page import BasePage
from models.lead import Lead

class Leads(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://hrm.anhtester.com/erp/leads-list'
        self.btnaddnew = self.page.get_by_role('link', name='Add New')
        self.firstname = self.page.get_by_role('textbox', name='First Name')
        self.lastname = self.page.get_by_role('textbox', name='Last Name')
        self.gender = self.page.locator('//select[@name="gender"]')
        self.contact = self.page.locator('//input[@name="contact_number"]')
        self.email = self.page.get_by_role('textbox', name='Email')
        self.file = self.page.locator('//input[@type="file"]')
        self.btnsave = self.page.get_by_role('button', name='Save')
        self.name = self.page.locator('//table[@id="xin_table"]//td[1]')
        self.search = self.page.get_by_role('searchbox', name='Search')

    def goto(self):
        self.navigate(self.url)

    def add_lead(self, lead: Lead):
        self.click(self.btnaddnew)
        self.set_text(self.firstname, lead.firstname)
        self.set_text(self.lastname, lead.lastname)
        self.select_dropdown(self.gender, lead.gender, by_label=False)
        self.set_text(self.contact, lead.contactnumber)
        self.set_text(self.email, lead.email)
        self.upload_file(self.file, lead.image_path)
        self.click(self.btnsave)

    def verify_lead(self, lead: Lead):
        self.set_text(self.search, lead.email)
        self.verify_element_text(self.name, lead.lastname, is_exact= False)