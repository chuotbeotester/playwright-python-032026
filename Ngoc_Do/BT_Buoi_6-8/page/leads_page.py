from playwright.sync_api import Page
from page.base_page import BasePage
from utils.path_helper import PathFile
from utils.lead import Lead


class ManageLeadsPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/leads-list"
    # Ảnh đại diện (Profile Picture) là trường BẮT BUỘC của form Add Lead.
    PROFILE_PICTURE = "upload_files/test_lead.png"

    def __init__(self, page: Page):
        super().__init__(page)
        self.link_add_new = self.page.get_by_role("link", name="Add New", exact=True)
        self.add_form = self.page.locator("#add_form")
        self.textbox_first_name = self.add_form.get_by_placeholder("First Name", exact=True)
        self.textbox_last_name = self.add_form.get_by_placeholder("Last Name", exact=True)
        self.textbox_email = self.add_form.get_by_placeholder("Email", exact=True)
        self.textbox_contact_number = self.add_form.get_by_placeholder("Contact Number", exact=True)
        self.input_profile_picture = self.add_form.locator('input[type="file"][name="file"]')
        self.button_save = self.add_form.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)
        self.button_delete_first_row = self.page.locator(
            '//table[@id="xin_table"]//tbody/tr[1]//button[contains(@class,"delete")]'
        )
        self.delete_modal = self.page.locator(".delete-modal")
        self.button_confirm_delete = self.delete_modal.get_by_role("button", name="Confirm", exact=True)
        # Lead vừa tạo — dùng để dọn dữ liệu sau khi test xong.
        self.created_lead = None

    def go_to_manage_leads_page(self):
        """Truy cập trang Manage Leads và xác minh trang đã sẵn sàng."""
        self.navigate(self.URL)
        self.verify_element_visible(self.link_add_new)

    def create_lead(self, lead: Lead):
        """Tạo một Lead mới: mở form Add New, nhập các trường bắt buộc và lưu.

        Args:
            lead (Lead): Bộ dữ liệu Lead cần tạo.
        """
        self.click(self.link_add_new)
        self.verify_element_visible(self.textbox_first_name)
        self.set_text(self.textbox_first_name, lead.first_name)
        self.set_text(self.textbox_last_name, lead.last_name)
        self.set_text(self.textbox_contact_number, lead.contact_number)
        self.set_text(self.textbox_email, lead.email)
        # Profile Picture bắt buộc — thiếu sẽ bị lỗi "The profile picture field is required."
        self.upload_file(self.input_profile_picture, PathFile.get_string_file_path(self.PROFILE_PICTURE))
        self.click(self.button_save)
        # Ghi nhận để dọn dữ liệu test sau khi chạy xong.
        self.created_lead = lead

    def verify_create_success(self, lead: Lead):
        """Xác minh tạo Lead thành công bằng cách tìm kiếm trong bảng "List All Leads".

        Args:
            lead (Lead): Lead vừa tạo, dùng first_name để tìm kiếm và đối chiếu.
        """
        self.set_text(self.textbox_search, lead.first_name)
        cell_lead_name = self.page.locator('//table[@id="xin_table"]//tbody/tr[1]/td[1]')
        self.verify_element_text(cell_lead_name, lead.first_name, is_exact=False)

    def delete_lead(self, lead: Lead = None):
        """Xóa một Lead rồi xác nhận. Dùng cho teardown để dọn dữ liệu test.

        Args:
            lead (Lead, optional): Lead cần xóa. Mặc định None → xóa Lead vừa tạo
                (self.created_lead). Không làm fail test nếu xóa lỗi.
        """
        lead = lead or self.created_lead
        if lead is None:
            return
        self.navigate(self.URL)
        try:
            self.set_text(self.textbox_search, lead.first_name)
            self.click(self.button_delete_first_row)
            self.verify_element_visible(self.button_confirm_delete)
            self.click(self.button_confirm_delete)
        except Exception as error:
            print(f"[cleanup] Không xóa được lead '{lead.first_name}': {error}")
        finally:
            self.created_lead = None
