import pytest
from playwright.sync_api import Page
from page.login_page import LoginPage
from page.core_hr.department_page import DepartmentPage
from page.core_hr.designation_page import DesignationPage
from page.core_hr.policies_page import PoliciesPage
from utils.path_helper import PathFile
from utils.text_data import TextData

config_data = PathFile.read_json_data('input_data/config.json')
URL = config_data['URL']
USERNAME = config_data['USERNAME']
PASSWORD = config_data['PASSWORD']
NAME_DEPARTMENT = TextData.create_text_data("New Department")

@pytest.mark.dependency(name="create_department")
def test_create_department(page: Page):
    """Kiểm thử quy trình tạo Department mới: đăng nhập, điều hướng tới trang Department,
    tạo Department mới và xác minh việc tạo thành công trong danh sách.

    Args:
        page (Page): Đối tượng Page của Playwright.
    """
    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    department_page = DepartmentPage(page)
    department_page.go_to_department_page()
    department_page.create_department(NAME_DEPARTMENT)
    department_page.verify_create_success(NAME_DEPARTMENT)

@pytest.mark.dependency(depends=["create_department"])
def test_create_designation(page: Page):
    """Kiểm thử quy trình tạo Designation mới gắn liền với phòng ban: đăng nhập, điều hướng tới
    trang Designation, tạo Designation mới và xác minh việc tạo thành công trong danh sách.

    Args:
        page (Page): Đối tượng Page của Playwright.
    """
    name_designation = TextData.create_text_data("New Designation")

    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    designation_page = DesignationPage(page)
    designation_page.go_to_designation_page()
    designation_page.create_designation(NAME_DEPARTMENT, name_designation)
    designation_page.verify_create_success(NAME_DEPARTMENT, name_designation)

def test_create_policies(page: Page):
    """Kiểm thử quy trình tạo Policies mới có mô tả và tệp đính kèm: đăng nhập,
    điều hướng tới trang Policies, tạo Policies mới và xác minh việc tạo thành công.

    Args:
        page (Page): Đối tượng Page của Playwright.
    """
    name_policy = TextData.create_text_data("New Policy")
    policy_description = TextData.create_text_data("New Policy Description")
    file_path = PathFile.get_string_file_path("upload_files/test_policies.png")

    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    policies_page = PoliciesPage(page)
    policies_page.go_to_policies_page()
    policies_page.create_policies(name_policy, policy_description, file_path)
    policies_page.verify_create_success(name_policy)