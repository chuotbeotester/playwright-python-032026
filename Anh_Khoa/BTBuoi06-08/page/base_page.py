from playwright.sync_api import Page, Locator, Error as PlaywrightError, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        try:
            self.page.goto(url)
        except PlaywrightError as e:
            raise PlaywrightError(f"Không thể navigate đến URL: {url}") from e

    def click(self, element_locator: Locator):
        try:
            element_locator.click()
        except PlaywrightError as e:
            raise PlaywrightError(f"Không thể click vào element: {element_locator}") from e

    def set_text(self, element_locator: Locator, input_value: str):
        try:
            element_locator.fill(input_value)
        except PlaywrightError as e:
            raise PlaywrightError(f"Không thể nhập '{input_value}' vào element: {element_locator}") from e

    def select_dropdown(self, element_locator: Locator, option: str, by_label: bool = False):
        try:
            if by_label:
                element_locator.select_option(label=option)
            else:
                element_locator.select_option(value=option)
        except PlaywrightError as e:
            select_by = "label" if by_label else "value"
            raise PlaywrightError(f"Không thể chọn option '{option}' (by {select_by}): {element_locator}") from e

    def upload_file(self, element_locator: Locator, file_path: str):
        try:
            element_locator.set_input_files(file_path)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Không tìm thấy file: '{file_path}'") from e
        except PlaywrightError as e:
            raise PlaywrightError(f"Không thể upload '{file_path}' vào: {element_locator}") from e

    def verify_element_visible(self, element_locator: Locator):
        try:
            expect(element_locator).to_be_visible()
        except AssertionError as e:
            raise AssertionError(f"Element không hiển thị: {element_locator}") from e

    def verify_element_text(self, element_locator: Locator, expected_text: str, is_exact: bool = True):
        try:
            if is_exact:
                expect(element_locator).to_have_text(expected_text)
            else:
                expect(element_locator).to_contain_text(expected_text)
        except AssertionError as e:
            mode = "exact" if is_exact else "contains"
            raise AssertionError(
                f"Verify text thất bại | Element: {element_locator} | Expected: '{expected_text}' | Mode: {mode}"
            ) from e
