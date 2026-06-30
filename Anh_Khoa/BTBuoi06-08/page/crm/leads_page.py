from playwright.sync_api import Page
from page.base_page import BasePage
from page.home_page import HomePage


class LeadsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.home_page = HomePage(page)

        self.button_add_new = self.page.get_by_role("link", name="Add New", exact=True)

        self.input_first_name = self.page.get_by_role("textbox", name="First Name", exact=True)
        self.input_last_name = self.page.get_by_role("textbox", name="Last Name", exact=True)
        self.select_gender = self.page.locator('select[name="gender"]')
        self.input_contact_number = self.page.get_by_placeholder("Contact Number")
        self.input_email = self.page.get_by_role("textbox", name="Email", exact=True)
        self.input_file = self.page.locator('input[name="file"]')
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)

        self.textbox_search = self.page.get_by_role("searchbox")
        self.cell_first_row_name = self.page.locator('#xin_table tbody tr:first-child td:first-child')

    def go_to_leads_page(self):
        self.home_page.choose_left_menu("Leads")
        self.verify_element_visible(self.button_add_new)

    def create_lead(
        self,
        first_name: str,
        last_name: str,
        gender: str,
        contact_number: str,
        email: str,
        file_path: str,
    ):
        """Điền form và lưu lead; timeout sau save để chờ redirect hoàn tất trước khi bước tiếp theo chạy."""
        self.click(self.button_add_new)
        self.set_text(self.input_first_name, first_name)
        self.set_text(self.input_last_name, last_name)
        self.select_dropdown(self.select_gender, gender, by_label=True)
        self.set_text(self.input_contact_number, contact_number)
        self.set_text(self.input_email, email)
        self.upload_file(self.input_file, file_path)
        self.click(self.button_save)
        self.page.wait_for_load_state("networkidle")

    def verify_lead_created(self, first_name: str, last_name: str):
        """Tìm kiếm theo first_name; expect tự retry đến khi bảng lọc xong."""
        self.set_text(self.textbox_search, first_name)
        self.verify_element_text(self.cell_first_row_name, f"{first_name} {last_name}", is_exact=False)
