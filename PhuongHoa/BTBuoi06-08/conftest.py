from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope = "session")
def browser_type():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope = "session")
def page(browser_type):
    context = browser_type.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()