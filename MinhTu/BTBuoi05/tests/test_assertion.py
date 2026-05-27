from playwright.sync_api import Page, expect
import time

def test_action(page : Page):
    page.goto("https://hrm.anhtester.com/")
    
    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    
    expect(page.get_by_role("textbox", name="Enter Password")).to_be_visible()
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
    page.locator("//label[@for='contact_number']/following-sibling::input").fill('0123')
    
    #Select Gender
    page.locator("//label[contains(text(), 'Gender')]/following-sibling::select").select_option(label='Female')
    
    #Input Email
    page.get_by_role("textbox", name="Email").fill('test@gmail.com')
    
    #Input Username
    page.get_by_role("textbox", name="Username").fill('tupham')
    
    #Upload File
    page.get_by_role("button", name="Choose File").set_input_files("tests/test.jpg")
    
    #Tap on Save button
    page.get_by_role("button", name="Save").click()
    
    #Verify Client added
    page.locator("//div[@id='toast-container']//div[text()='Client added.']").wait_for()
    
    #Search the existing email
    page.get_by_role("searchbox", name="Search").fill('test@gmail.com')
    
    # #Verify Name column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[1]//h6")).to_have_text('test test')
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[1]//p")).to_have_text('test@gmail.com')
    
    #Verify Username column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[2]")).to_contain_text('tupham')
    
    #Verify Contact Number column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[3]")).to_have_text('0123')
    
    #Verify Gender column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[4]")).to_have_text('Female')
    
    #Verify Status column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[6]")).to_have_text('Active')
    
    #Delete user
    btn_del = "//table[@id='xin_table']/tbody/tr[1]/td[1]//button[contains(@class, 'delete')]"
    # btn_confirm = "//button/span[text()='Confirm']"
    page.locator(btn_del).hover()
    page.locator(btn_del).click()
    page.get_by_role("button", name="Confirm").click()
    
    #Verify Client deleted
    page.locator("//div[@id='toast-container']//div[text()='Client deleted.']").wait_for()