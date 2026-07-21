import re
from playwright.sync_api import Playwright, Page, sync_playwright, expect
import time

def test_add_user(page : Page):
    # Go to login page
    page.goto("https://hrm.anhtester.com/")

    firstName = "Duy"
    lastName = "Quang"
    password = "123456"
    contactNumber = "0123456789"
    email = "liu99@gmail.com"
    userName = "DuyQuang"
    gender = "Male"

    # Input username
    page.get_by_role("textbox", name="Your Username").fill("admin_example")

    # Input password
    page.get_by_role("textbox", name="Enter Password").fill("123456")

    # Click Login button    
    page.locator("//i[@class='fas fa-user-lock d-blockd']").click()

    # Click Manage Clients menu
    page.get_by_role("link", name="Manage Clients").click()

    # ACTION
    # Click Add new
    page.get_by_role("link", name="Add New").click()

    # Input First name
    page.get_by_role("textbox", name="First Name").fill(firstName)

    # Input Last name
    page.get_by_role("textbox", name="Last Name").fill(lastName)

    # Input password
    page.get_by_role("textbox", name="Password").fill(password)

    # Input Contact number
    page.locator("//input[@name='contact_number']").fill(contactNumber)

    # Select Gender
    page.locator("//select[@class='form-control select2-hidden-accessible']").select_option(label=gender)

    # Input Email
    page.get_by_role("textbox", name="Email").fill(email)

    # Input Username
    page.get_by_role("textbox", name="Username").fill(userName)

    # Attach file
    page.locator('//input[@class="custom-file-input"]').set_input_files("DuyQuang/BT_Buoi5/tests/uploadimg.png")

    # Click save button
    page.get_by_role("button", name="Save").click()

    # Search for user by email
    page.get_by_role("searchbox", name="Search").fill(email)


    # ASSERTIONS
    # Verify search results

    # Verify Name
    expect(page.locator("//h6[@class='m-b-0']")).to_have_text(firstName+" "+lastName)

    # Verify Email
    expect(page.locator("//p[@class='m-b-0']")).to_have_text(email)

    # Verify UserName
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[1]")).to_have_text(userName)

    # Verify Phone
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[2]")).to_have_text(contactNumber)

    # Verify Gender
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[3]")).to_have_text(gender)

    # Verify Status
    expect(page.locator("//span[@class='badge badge-light-success']")).to_have_text("Active")

   






