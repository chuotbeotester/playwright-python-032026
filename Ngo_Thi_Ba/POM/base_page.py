from playwright.async_api import Page

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        

def click(self, locator):
    self.page.locator(locator).click()
    
def fill_text(self,locator,text):
    self.page.locator(locator).fill(text)
    
def verify_element_visible(self,locator):
    self.page.locator(locator).is_visible()
    
def verify_element_text(self, locator, expected_text):
    self.page.locator(locator).to_have_text(expected_text)
    
def select_dropdown(self,locator,choice):
    self.page.locator(locator).select_option(choice)
    
def upload_file(self,locator,file_path):
    self.page.locator(locator).set_input_files(file_path)
    
def navigate_URL (self,url):
    self.page.goto(url)
