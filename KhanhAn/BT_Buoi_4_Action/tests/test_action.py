from playwright.sync_api import Page
from faker import Faker
import time

fake = Faker()
username = f"test{int(time.time())}"
email = f"{username}@gmail.com"
first_name = fake.first_name()
last_name = fake.last_name()
password = fake.password(length=10)
contact_number = fake.numerify("09########")
    
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
    page.locator("input[type='file']").set_input_files("KhanhAn/BT_Buoi_4_Action/data/test_upload.jpg")
    
    # Click the Save button
    page.get_by_role("button", name="Save").click()