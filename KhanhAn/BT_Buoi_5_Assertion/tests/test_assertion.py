from playwright.sync_api import Page,expect
from faker import Faker
import time

def test_assertion(page : Page):
    fake = Faker()

    # Generate random test data
    username = f"test{int(time.time())}"
    email = f"{username}@gmail.com"
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password(length=10)
    contact_number = fake.numerify("09########")

    # Data login
    username_login = "admin_example"
    password_login = "123456"
    url_login = "https://hrm.anhtester.com/"
    url_manage_clients = "https://hrm.anhtester.com/erp/clients-list"


    # Open Login HRM website
    page.goto(url_login)
    page.get_by_role("textbox", name="Your Username").fill(username_login)
    page.get_by_role("textbox", name="Enter Password").fill(password_login)
    btn_login = page.locator('//button[contains(@class, "btn-primary")]')
    btn_login.click()
    expect(page).to_have_url(url_login)

    loading_modal = page.get_by_role("dialog", name="Logged In Successfully.")
    expect(loading_modal).to_be_visible()
    expect(loading_modal).to_be_hidden()

    #Select Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    expect(page).to_have_url(url_manage_clients)

    #Click Add New
    page.get_by_role("link", name="Add New").click()

    #Input First Name
    page.get_by_role("textbox", name="First Name").fill(first_name)

    #Input Last Name
    page.get_by_role("textbox", name="Last Name").fill(last_name)

    #Input Password
    page.get_by_role("textbox", name="Password").fill(password)

    #Input Contact Number
    page.locator("//input[@name='contact_number']").fill(contact_number)

    #Select Gender
    page.locator("//select[@name='gender']").select_option(label='Male')

    #Input Email
    page.get_by_role("textbox", name="Email").fill(email)

    #Input Username
    page.get_by_role("textbox", name="Username").fill(username)

    #Upload File
    page.locator("input[type='file']").set_input_files("KhanhAn/BT_Buoi_5_Assertion/data/test_upload.jpg")

    # Click the Save button
    page.get_by_role("button", name="Save").click()
    expect(page.locator("//div[text()='Client added.']")).to_be_visible()


    # Search the existing email
    page.get_by_role("searchbox", name="Search").fill(email)

    #Verify Name column
    expect(page.locator("//div[@class='d-inline-block']/h6")).to_have_text(first_name+" "+last_name)
    expect(page.locator("//div[@class='d-inline-block']/p")).to_have_text(email)

    #Verify Username column
    expect(page.locator("//tr[@class='odd']/td[2]")).to_have_text(username)

    # Verify Contact Number column
    expect(page.locator("//tr[@class='odd']/td[3]")).to_have_text(contact_number)

    #Verify Gender column
    expect(page.locator("//tr[@class='odd']/td[4]")).to_have_text('Male')

    #Verify Status column
    expect(page.locator("//tr[@class='odd']/td[6]")).to_have_text('Active')

    #Delete user flow - for clear data function (bonus)
    # locator list
    delete_modal = page.locator("//h5[contains(text(), 'Are you sure you want to delete this record?')]/ancestor::div[@class='modal-content']")
    delete_btn = page.locator("//button[contains(@class, 'delete')]")

    # Action
    delete_btn.hover()
    delete_btn.click()
    expect(delete_modal).to_be_visible()
    page.locator("//span[text()='Confirm']/ancestor::button").click()
    expect(page.locator("//div[text()='Client deleted.']")).to_be_visible()