import pytest
from page import DepartmentPage, DesignationPage, PoliciesPage, ManageClientPage, LeadsPage
from utils.path_helper import PathFile
from utils.text_data import TextData


# --- Core HR ---

@pytest.fixture
def department_page(logged_in_page) -> DepartmentPage:
    return DepartmentPage(logged_in_page)


@pytest.fixture
def designation_page(logged_in_page) -> DesignationPage:
    return DesignationPage(logged_in_page)


@pytest.fixture
def policies_page(logged_in_page) -> PoliciesPage:
    return PoliciesPage(logged_in_page)


# --- CRM ---

@pytest.fixture
def manage_client_page(logged_in_page) -> ManageClientPage:
    return ManageClientPage(logged_in_page)


@pytest.fixture
def manage_client_data() -> dict:
    """Đọc JSON và sinh first_name, email, username duy nhất theo timestamp để tránh trùng dữ liệu giữa các lần chạy."""
    data = PathFile.read_json_data("input_data/manage_client_data.json")
    return {
        **data,
        "first_name": TextData.create_text_data(data["first_name_prefix"]),
        "email": TextData.create_unique_email(data["email_prefix"], data["email_domain"]),
        "username": TextData.create_unique_username(data["username_prefix"]),
        "file_path": PathFile.get_string_file_path(data["upload_file"]),
    }


@pytest.fixture
def leads_page(logged_in_page) -> LeadsPage:
    return LeadsPage(logged_in_page)


@pytest.fixture
def leads_data() -> dict:
    """Đọc JSON và sinh first_name, email duy nhất theo timestamp để tránh trùng dữ liệu giữa các lần chạy."""
    data = PathFile.read_json_data("input_data/leads_data.json")
    return {
        **data,
        "first_name": TextData.create_text_data(data["first_name_prefix"]),
        "email": TextData.create_unique_email(data["email_prefix"], data["email_domain"]),
        "file_path": PathFile.get_string_file_path(data["upload_file"]),
    }
