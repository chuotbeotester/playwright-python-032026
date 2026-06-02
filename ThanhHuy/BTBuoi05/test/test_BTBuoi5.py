from playwright.sync_api import Page, expect
import time

# data test
first_name = "ThanhHuy"
last_name = "Nguyen"
password = "11112222"
contact_number = "01233221"
email = "thanhhuy@gmail.com"
username = "thanhhuy1998"
gender = "Male"
file_path = "ThanhHuy/BTBuoi05/data/image_uploaded.png"

# locators
login_url = "https://hrm.anhtester.com/erp/login"
login_username_locator = "//input[@id='iusername']"
login_password_locator = "//input[@id='ipassword']"
login_button_locator = '//button[contains(@class,"btn-primary")]'
manage_clients_menu_locator = '//span[normalize-space()="Manage Clients"]'
add_new_button_locator = '//a[normalize-space()="Add New"]'
first_name_locator = "//input[@placeholder='First Name']"
last_name_locator = "//input[@placeholder='Last Name']"
password_locator = "//input[@placeholder='Password']"
contact_number_locator = "//input[@placeholder='Contact Number']"
email_locator = "//input[@placeholder='Email']"
username_locator = "//input[@placeholder='Username']"
gender_locator = "//select[@name='gender']"
file_upload_locator = "//input[@name='file']"
save_button_locator = "//span[normalize-space()='Save']"
search_input_locator = "//input[@type='search']"

def test_assertion_bai5(page:Page):
    # Login
    page.goto(login_url)
    page.fill(login_username_locator, "admin_example")
    page.fill(login_password_locator, "123456")
    page.click(login_button_locator)

    # Navigate to Manage Clients
    page.click(manage_clients_menu_locator)

    # Click on Add New button
    page.click(add_new_button_locator)

    # Fill in the form
    page.fill(first_name_locator, first_name)
    page.fill(last_name_locator, last_name)
    page.fill(password_locator, password)
    page.fill(contact_number_locator, contact_number)
    page.fill(email_locator, email)
    page.fill(username_locator, username)
    page.select_option(gender_locator, gender)
    page.set_input_files(file_upload_locator, file_path)    
    page.click(save_button_locator)

    # Search the client added by email
    page.fill(search_input_locator, email)

    # Verify the client information in the table

    #Name
    expect(page.locator("//tbody/tr/td[1]")).to_contain_text(f"{first_name} {last_name}")
    #Email
    expect(page.locator("//tbody/tr/td[1]")).to_contain_text(email)
    #Username
    expect(page.locator("//tbody/tr/td[2]")).to_contain_text(username)
    #Contact Number
    expect(page.locator("//tbody/tr/td[3]")).to_contain_text(contact_number)
    #Gender
    expect(page.locator("//tbody/tr/td[4]")).to_contain_text(gender)
    #Status
    expect(page.locator("//tbody/tr/td[6]")).to_contain_text("Active")