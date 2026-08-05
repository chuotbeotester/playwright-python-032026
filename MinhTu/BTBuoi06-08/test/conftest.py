import pytest, time
from utils.path_helper import PathFile
from page import LoginPage, HomePage, ManageClientPage, LeadsPage



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
def manage_client(page):
    manage_client = ManageClientPage(page)
    yield manage_client
    
@pytest.fixture
def leads(page):
    leads = LeadsPage(page)
    yield leads