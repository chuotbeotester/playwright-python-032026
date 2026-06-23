from playwright.sync_api import Page
from page.base_page import BasePage

class ManageClientPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.btn_addNew = self.page.get_by_role("link", name="Add New")
        self.textbox_firstName = self.page.get_by_role("textbox", name="First Name")
        self.textbox_lastName = self.page.get_by_role("textbox", name="Last Name")
        self.textbox_password = self.page.get_by_role("textbox", name="Password")
        self.textbox_contactNumber = self.page.locator('//input[@name="contact_number"]')
        self.dropdown_gender = self.page.locator('//select[@class="form-control select2-hidden-accessible"]')
        self.textbox_email = self.page.get_by_role("textbox", name="Email")
        self.textbox_userName = self.page.get_by_role("textbox", name="Username")
        self.uploadFile = self.page.locator('//input[@class="custom-file-input"]')
        self.btn_save = self.page.get_by_role("button", name="Save")
        
        self.textbox_search = self.page.get_by_role("searchbox", name="Search")
        self.table_name = self.page.locator('//h6[@class="m-b-0"]')
        self.table_email = self.page.locator('//p[@class="m-b-0"]')
        self.table_username = self.page.locator('//td[@class="sorting_1"]/following-sibling::td[1]')
        self.table_contactNumber = self.page.locator('//td[@class="sorting_1"]/following-sibling::td[2]')
        self.table_gender = self.page.locator('//td[@class="sorting_1"]/following-sibling::td[3]')
        
    def go_to_manage_client_page(self):
       self.navigate("https://hrm.anhtester.com/erp/clients-list")

    def add_new_client(self, firstName: str, lastName: str, password: str, contactNumber: int, gender, email: str, userName: str, uploadFile):
        self.set_text(self.textbox_firstName, firstName)
        self.set_text(self.textbox_lastName, lastName)
        self.set_text(self.textbox_password, password)
        self.set_text(self.textbox_contactNumber, contactNumber)
        self.select_dropdown(self.dropdown_gender, gender)
        self.set_text(self.textbox_email, email)
        self.set_text(self.textbox_userName, userName)
        self.upload_file(self.uploadFile, uploadFile)
        self.click(self.btn_save)

    def verify_added_client(self, firstName: str, lastName: str, contactNumber: int, gender, email: str, userName: str):
        self.set_text(self.textbox_search, email)
        self.verify_element_text(self.table_name, firstName+" "+lastName)
        self.verify_element_text(self.table_email, email)
        self.verify_element_text(self.table_username, userName)
        self.verify_element_text(self.table_contactNumber,contactNumber)
        self.verify_element_text(self.table_gender, gender)
