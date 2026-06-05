from playwright.sync_api import Page, expect
import time

# data test
first_name = "ThHuy"
last_name = "Nguyen"
password = "111122"
contact_number = "01233241"
email = "thanhhuy123@gmail.com"
username = "thhuy1998"
file_path = "ThanhHuy/BTBuoi05/data/image_uploaded.png"

# locators
login_url = "https://hrm.anhtester.com/erp/login"


def test_assertion_bai5(page:Page):
    # Access the login page
    page.goto(login_url)

    #Input username and password, then click on the login button
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    login_button = page.locator('//button[contains(@class,"btn-primary")]')
    login_button.click()

    # Click to Manage Clients
    page.get_by_role("link", name="Manage Clients").click()

    # Click on Add New button
    page.get_by_role("link", name="Add New").click()

    # Fill in the form
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").fill(last_name)
    page.get_by_role("textbox", name="Password").fill(password)
    page.locator("//input[@placeholder='Contact Number']").fill(contact_number)
    page.locator("//select[@name='gender']").select_option(label="Male")
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Username").fill(username)
    page.locator("//input[@name='file']").set_input_files(file_path)
    page.get_by_role("button", name="Save").click()

    # Search the client added by email
    page.get_by_role("searchbox", name="Search").fill(email)

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
    expect(page.locator("//tbody/tr/td[4]")).to_contain_text("Male")
    #Status
    expect(page.locator("//tbody/tr/td[6]")).to_contain_text("Active")