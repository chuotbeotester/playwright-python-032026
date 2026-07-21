from playwright.sync_api import Page
import time
def test_actions(page: Page):
    
    page.goto("https://crm.anhtester.com/admin/authentication")
    time.sleep(3)
    page.locator("#remember").click()
    time.sleep(3)
    page.locator("#remember").click()
    time.sleep(3)