
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from utils.path_helper import PathFile
from page.lead_page import LeadsPage
from page.manage_clients_page import ManageClientsPage



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
def logged_in_leads(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    homePage = HomePage(page)
    homePage.choose_left_menu("Leads")
    
    yield LeadsPage(page)


@pytest.fixture
def logged_in_manage_clients(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    manageClientsPage = ManageClientsPage(page)
    yield manageClientsPage
