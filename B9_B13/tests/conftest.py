from playwright.sync_api import sync_playwright
import pytest, string, random
from pages.UI.login_page import LoginPage
from pages.UI.home_page import HomePage
from pages.UI.project.project_page import Project

@pytest.fixture(scope="function")
def login(page):
    return LoginPage(page)

@pytest.fixture
def logged_in_home(page, login):
    login.goto("https://hrm.anhtester.com/erp/login")
    login.login("admin_example", "123456")
    homePage = HomePage(page)
    yield homePage

@pytest.fixture
def logged_in_project(page, login):
    login.goto("https://hrm.anhtester.com/erp/login")
    login.login("admin_example", "123456")
    project = Project(page)
    yield project


@pytest.fixture
def loggedin_home_storage(browser_instance):
    context = browser_instance.new_context(
        storage_state= "tests/storage_stage.json"
    )

    page = context.new_page()
    home_page = HomePage(page)

    yield home_page

    context.close()


