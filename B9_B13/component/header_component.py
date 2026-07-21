from playwright.sync_api import Page, expect, TimeoutError, Locator

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.accountSetting = self.page.locator("...")

    def click_accountsetting(self):
        self.accountSetting.click()
