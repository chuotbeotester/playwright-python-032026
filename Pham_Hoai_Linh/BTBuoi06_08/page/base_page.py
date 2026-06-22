from playwright.async_api import Page, Locator, Error as PlaywrightError, expect

class BasePage:
    def __init__ (self, page: Page):
        self.page = page

    def click(self, locator: Locator):
        locator.click()

    def set_text(self, locator: Locator, input_value: str):
        locator.fill(input_value)

    def navigate_to(self, url: str):
        self.page.goto(url)

    def select_dropdown(self, locator: Locator, option):
        locator.select_option(label=option)

    def upload_file(self, locator: Locator, file_path):
        locator.set_input_files(file_path)

    def verify_element_visible(self, locator: Locator):
        expect(locator).to_be_visible

    def verify_element_text(self, element_locator: Locator, expected_text: str, is_exact: bool = True):
        try:
            if is_exact:
                expect(element_locator).to_have_text(expected_text)
            else:
                expect(element_locator).to_contain_text(expected_text)
        except PlaywrightError as e:
            mode = "have_text" if is_exact else "contains_text"
            raise PlaywrightError(
                f"Verify text thất bại | Element: {element_locator} "
                f"| Expected: '{expected_text}' | Mode: {mode}"
            ) from e 