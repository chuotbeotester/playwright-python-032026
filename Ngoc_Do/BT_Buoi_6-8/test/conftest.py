import pytest
from utils.path_helper import PathFile
from utils.client import Client
from page import (
    LoginPage,
    HomePage,
    DepartmentPage,
    DesignationPage,
    PoliciesPage,
    ManageClientsPage,
    ManageLeadsPage,
)



@pytest.fixture(scope ="session")
def get_credential():
    credential = PathFile.read_json_data("input_data/config.json")
    yield credential

@pytest.fixture(scope="function")
def login(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_home(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    homePage = HomePage(page)
    yield homePage


@pytest.fixture
def logged_in_department(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    departmentPage = DepartmentPage(page)

    yield departmentPage


@pytest.fixture
def logged_in_designation(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    designation = DesignationPage(page)
    yield designation


@pytest.fixture
def logged_in_policy(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    policy = PoliciesPage(page)
    yield policy



@pytest.fixture
def logged_in_manage_clients(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    manage_clients = ManageClientsPage(page)
    yield manage_clients
    # Teardown: xóa Client vừa tạo trong test để không để lại dữ liệu rác.
    manage_clients.delete_client()


@pytest.fixture
def add_new_client(logged_in_manage_clients):
    new_client = Client.create_text_data()
    logged_in_manage_clients.go_to_manage_clients_page()
    logged_in_manage_clients.create_client(new_client)
    logged_in_manage_clients.verify_create_success(new_client)
    yield new_client


@pytest.fixture
def logged_in_manage_leads(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    manage_leads = ManageLeadsPage(page)
    yield manage_leads
    # Teardown: xóa Lead vừa tạo trong test để không để lại dữ liệu rác.
    manage_leads.delete_lead()