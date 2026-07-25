from page.base_page  import BasePage

class Leads(BasePage):
    def __init__(self, page):
        super().__init__(page)
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

    def goto(self, url: str):
        self.navigate(url)

    def add_lead(self, firstname: str, lastname: str, gender: str, contact: str, email: str, path_file: str):
        self.click(self.btnaddnew)
        self.set_text(self.firstname, firstname)
        self.set_text(self.lastname, lastname)
        self.select_dropdown(self.gender, gender, by_label=False)
        self.set_text(self.contact, contact)
        self.set_text(self.email, email)
        self.upload_file(self.file, path_file)
        self.click(self.btnsave)

    def verify_lead(self, search_text: str, expected_name: str):
        self.set_text(self.search, search_text)
        self.verify_element_text(self.name, expected_name, is_exact= False)