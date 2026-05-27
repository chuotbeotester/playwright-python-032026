from playwright.sync_api import Page
import time

def test_action(page : Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    btn_login = page.locator('//button[contains(@class, "btn-primary")]')
    btn_login.click()
    
    #Select Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    
    #Click Add New
    page.get_by_role("link", name="Add New").click()
    
    #Input First Name
    page.get_by_role("textbox", name="First Name").fill('test')
    
    #Input Last Name
    page.get_by_role("textbox", name="Last Name").fill('test')
    
    #Input Password
    page.get_by_role("textbox", name="Password").fill('123456')
    
    #Input Contact Number
    page.locator("//label[@for='contact_number']/following-sibling::input").fill('0123456789')
    
    #Select Gender
    page.locator("//label[contains(text(), 'Gender')]/following-sibling::select").select_option(label='Female')
    
    #Input Email
    page.get_by_role("textbox", name="Email").fill('test@gmail.com')
    
    #Input Username
    page.get_by_role("textbox", name="Username").fill('test12345')
    
    #Upload File
    page.get_by_role("button", name="Choose File").set_input_files("tests/test.jpg")
    
    #Tap on Save button
    page.get_by_role("button", name="Save").click()