from playwright.sync_api import Page, expect, TimeoutError, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _goto(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def _click(self, locator: Locator):
        locator.click()

    def _fill(self, locator: Locator, text: str):
        locator.fill(text)

    def _assert_visible(self, locator: Locator):
        expect(locator).to_be_visible()
    
    def _assert_disable(self, locator: Locator):
        expect(locator).not_to_be_visible()

    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")


    def _click_open_new_tab(self, locator : Locator, timeout : int = 10000):
        with self.page.context.expect_page(timeout = timeout) as new_page:
            locator.click()
        
        new_page_info = new_page.value
        new_page_info.wait_for_load_state("load")
        return new_page_info
    
    def _bring_to_front(self):
        self.page.bring_to_front()
    
    def _page_close(self):
        self.page.close()
    

    
