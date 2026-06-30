import pytest
from utils.text_data import TextData


NAME_DEPARTMENT = TextData.create_text_data("New Department")

def test_create_department(logged_in_department):
    logged_in_department.go_to_department_page()
    logged_in_department.create_department(NAME_DEPARTMENT)
    logged_in_department.verify_create_success(NAME_DEPARTMENT)
