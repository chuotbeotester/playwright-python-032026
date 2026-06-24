import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from utils.path_helper import PathFile
from page.manage_client_page import ManageClientPage
from page.leads_page import LeadsPage

@pytest.fixture(scope="session")
# Đọc dữ liệu từ file json, bằng cách gọi phương thức read json từ class Pathfile
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
def logged_in_manageClient(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    manageClientPage = ManageClientPage(page)
    yield manageClientPage

@pytest.fixture
def logged_in_lead(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    leadsPage = LeadsPage(page)
    yield leadsPage

@pytest.fixture
def get_client_infor():
    clientInfor = PathFile.read_json_data("input_data/new_client.json")
    yield clientInfor