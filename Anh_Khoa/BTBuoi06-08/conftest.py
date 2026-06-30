import pytest
from playwright.sync_api import sync_playwright, expect
from page import LoginPage
from page.home_page import HomePage
from utils.path_helper import PathFile


@pytest.fixture(scope="session")
def browser():
    """Launch Chromium 1 lần duy nhất cho toàn bộ test session."""
    with sync_playwright() as playwright:
        b = playwright.chromium.launch(headless=False, slow_mo=300)
        yield b
        b.close()


@pytest.fixture(scope="function")
def logged_in_page(browser):
    """Mỗi test nhận 1 context/tab mới và login lại qua UI, đảm bảo cô lập hoàn toàn
    state giữa các test."""
    context = browser.new_context()
    pg = context.new_page()
    config = PathFile.read_json_data("input_data/config.json")
    login_page = LoginPage(pg)
    login_page.login(config["URL"], config["USERNAME"], config["PASSWORD"])
    # Chờ menu trái hiển thị để chắc chắn login hoàn tất, thay cho sleep cứng
    expect(HomePage(pg).left_menu).to_be_visible()
    yield pg
    context.close()
