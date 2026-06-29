import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.path_helper import PathFile
from pages import ManageClientsPage, LeadPage


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
def logged_in_manage_client(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    manageClientsPage = ManageClientsPage(page)

    yield manageClientsPage


@pytest.fixture
def logged_in_leads(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    leadsPage = LeadPage(page)
    yield leadsPage