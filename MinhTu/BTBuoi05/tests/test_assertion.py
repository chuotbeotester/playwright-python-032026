from playwright.sync_api import Page, expect
import time

firstName = 'test'
lastName = 'test'
pwd = '123456'
contactNumber = '0123'
email = 'test@gmail.com'
username = 'tupham'

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
    page.get_by_role("textbox", name="First Name").fill(firstName)
    
    #Input Last Name
    page.get_by_role("textbox", name="Last Name").fill(lastName)
    
    #Input Password
    page.get_by_role("textbox", name="Password").fill(pwd)
    
    #Input Contact Number
    page.locator("//label[@for='contact_number']/following-sibling::input").fill(contactNumber)
    
    #Select Gender
    page.locator("//label[contains(text(), 'Gender')]/following-sibling::select").select_option(label='Female')
    
    #Input Email
    page.get_by_role("textbox", name="Email").fill(email)
    
    #Input Username
    page.get_by_role("textbox", name="Username").fill(username)
    
    #Upload File
    page.get_by_role("button", name="Choose File").set_input_files("tests/test.jpg")
    
    #Tap on Save button
    page.get_by_role("button", name="Save").click()
    
    #Verify Client added
    page.locator("//div[@id='toast-container']//div[text()='Client added.']").wait_for()
    
    #Search the existing email
    page.get_by_role("searchbox", name="Search").fill(email)
    
    # #Verify Name column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[1]//h6")).to_have_text(f"{firstName} {lastName}")
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[1]//p")).to_have_text(email)
    
    #Verify Username column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[2]")).to_contain_text(username)
    
    #Verify Contact Number column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[3]")).to_have_text(contactNumber)
    
    #Verify Gender column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[4]")).to_have_text('Female')
    
    #Verify Status column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[6]")).to_have_text('Active')
    
    #Delete user
    del_btn = page.locator("//table[@id='xin_table']/tbody/tr[1]/td[1]//button[contains(@class, 'delete')]")    
    del_btn.hover()
    del_btn.click()
    
    modal = page.locator("//h5[contains(text(), 'Are you sure you want to delete this record?')]/ancestor::div[@class='modal-content']")
    confirm_btn = page.locator("//form[@id='delete_record']//button[@type='submit']")
    
    expect(modal).to_be_visible()
    expect(confirm_btn).to_be_visible()
    confirm_btn.click()
    expect(modal).to_be_hidden()
    
    #Verify Client deleted
    expect(page.locator("//div[@id='toast-container']//div[text()='Client deleted.']")).to_be_visible()