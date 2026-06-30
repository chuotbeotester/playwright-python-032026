import pytest
from page import DepartmentPage, DesignationPage, PoliciesPage
from utils.path_helper import PathFile
from utils.text_data import TextData

# Dùng chung giữa test_create_department và test_create_designation (dependency)
NAME_DEPARTMENT = TextData.create_text_data("New Department")


@pytest.mark.dependency(name="create_department")
def test_create_department(department_page: DepartmentPage):
    department_page.go_to_department_page()
    department_page.create_department(NAME_DEPARTMENT)
    department_page.verify_create_success(NAME_DEPARTMENT)


@pytest.mark.dependency(depends=["create_department"])
def test_create_designation(designation_page: DesignationPage):
    name_designation = TextData.create_text_data("New Designation")
    designation_page.go_to_designation_page()
    designation_page.create_designation(NAME_DEPARTMENT, name_designation)
    designation_page.verify_create_success(NAME_DEPARTMENT, name_designation)


def test_create_policies(policies_page: PoliciesPage):
    name_policy = TextData.create_text_data("New Policy")
    description = TextData.create_text_data("New Policy Description")
    file_path = PathFile.get_string_file_path("upload_files/ok.jpg")
    policies_page.go_to_policies_page()
    policies_page.create_policies(name_policy, description, file_path)
    policies_page.verify_create_success(name_policy)
