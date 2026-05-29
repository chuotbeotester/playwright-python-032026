from playwright.sync_api import Page, expect
from pathlib import Path
import time

#test data
firstName = 'test'
lastName = 'test'
pwd = '123456'
contactNumber = '0123'
email = 'test@gmail.com'
username = 'tupham'
gender = 'Female'
status = 'Active'

#locators
login_btn = '//button[contains(@class, "btn-primary")]'
contact_number_field = "//label[@for='contact_number']/following-sibling::input"
gender_field = "//label[contains(text(), 'Gender')]/following-sibling::select"
delete_btn = "//table[@id='xin_table']/tbody/tr[1]/td[1]//button[contains(@class, 'delete')]"
delete_modal = "//h5[contains(text(), 'Are you sure you want to delete this record?')]/ancestor::div[@class='modal-content']"
client_added_msg = "//div[@id='toast-container']//div[text()='Client added.']"
client_deleted_msg = "//div[@id='toast-container']//div[text()='Client deleted.']"
name_column = "//table[@id='xin_table']/tbody/tr[1]/td[1]//h6"
email_column = "//table[@id='xin_table']/tbody/tr[1]/td[1]//p"
username_column = "//table[@id='xin_table']/tbody/tr[1]/td[2]"
contact_number_column = "//table[@id='xin_table']/tbody/tr[1]/td[3]"
gender_column = "//table[@id='xin_table']/tbody/tr[1]/td[4]"
status_column = "//table[@id='xin_table']/tbody/tr[1]/td[6]"

def test_action(page : Page):
    page.goto("https://hrm.anhtester.com/")
    
    #Input username
    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    
    #Input password
    expect(page.get_by_role("textbox", name="Enter Password")).to_be_visible()
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    
    #Click Login button
    expect(page.locator(login_btn)).to_be_enabled()
    page.locator(login_btn).click()
    
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
    page.locator(contact_number_field).fill(contactNumber)
    
    #Select Gender
    page.locator(gender_field).select_option(label = gender)
    
    #Input Email
    page.get_by_role("textbox", name="Email").fill(email)
    
    #Input Username
    page.get_by_role("textbox", name="Username").fill(username)
    
    #Upload File
    file_path = Path(__file__).parent / "test.jpg"
    page.get_by_role("button", name="Choose File").set_input_files(str(file_path))
    
    #Tap on Save button
    page.get_by_role("button", name="Save").click()
    
    #Verify Client added
    expect(page.locator(client_added_msg)).to_be_visible()
    
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
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[4]")).to_have_text(gender)
    
    #Verify Status column
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[6]")).to_have_text(status)
    
    #Delete user
    confirm_btn = page.get_by_role("button", name="Confirm")
    
    page.locator(delete_btn).hover()
    page.locator(delete_btn).click()
    
    expect(page.locator(delete_modal)).to_be_visible()
    time.sleep(1)
    expect(confirm_btn).to_be_visible()
    confirm_btn.click()
    expect(page.locator(delete_modal)).to_be_hidden()
    
    #Verify Client deleted
    expect(page.locator(client_deleted_msg)).to_be_visible()