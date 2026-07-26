import pytest
from page.login_page import LoginPage
from page.leads_page import Leads
from utils.path_hepler import PathFile
from factories.lead_factory import LeadFactory



@pytest.fixture(scope ="session")
def get_credential():
    credential = PathFile.read_json_data("user_data/config.json")
    yield credential

@pytest.fixture(scope="function")
def login(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_lead(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    leadsPage = Leads(page)
    yield leadsPage
    
@pytest.fixture
def lead():
    return LeadFactory.create_leadfactory()