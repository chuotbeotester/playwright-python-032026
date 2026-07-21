from playwright.sync_api import sync_playwright
import pytest, string, random, asyncio


@pytest.fixture(scope = "session")
def playwright_instance():
    p = sync_playwright().start()
    yield p
    p.stop()


@pytest.fixture(scope = "session")
def browser_instance(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope = "session")
def page(browser_instance):
    context = browser_instance.new_context( viewport={'width': 1440, 'height': 900})

    page = context.new_page()
    yield page
    page.close()
    context.close()

def random_string(len:int):
    chars = string.ascii_lowercase
    return ''.join(random.choices(chars, k=len))

def random_email():
    email = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{email}@auto.com"

def random_string(len:int):
    chars = string.ascii_lowercase
    return ''.join(random.choices(chars, k=len))

def random_email():
    email = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{email}@auto.com"

@pytest.fixture(scope="session")
def api_context(playwright_instance):
        request_context = playwright_instance.request.new_context(
            base_url= "https://book.anhtester.com/",
            extra_http_headers= {
                "Accept" : "application/json"
            }
        )
        yield request_context
        request_context.dispose()

@pytest.fixture
def new_user_data():
    return {
            "name": random_string(8),
            "email": random_email(),
            "password": "Test@123",
            "avatarUrl": "",
            "phone": "0987654321",
            "address": "123 HCM"
}