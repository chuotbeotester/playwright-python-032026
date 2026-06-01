import re
from playwright.sync_api import Playwright, Page, sync_playwright, expect
import time

def test_add_user(page : Page):
    # Go to login page
    page.goto("https://hrm.anhtester.com/")

    # Input username
    page.get_by_role("textbox", name="Your Username").fill("admin_example")

    # Input password
    page.get_by_role("textbox", name="Enter Password").fill("123456")

    # Click Login button    
    page.locator("//i[@class='fas fa-user-lock d-blockd']").click()

    # Click Manage Clients menu
    page.get_by_role("link", name="Manage Clients").click()

    # Click Add new
    page.get_by_role("link", name="Add New").click()

    # Input First name
    page.get_by_role("textbox", name="First Name").fill("Liu")

    # Input Last name
    page.get_by_role("textbox", name="Last Name").fill("Quang")

    # Input password
    page.get_by_role("textbox", name="Password").fill("123456")

    # Input Contact number
    page.locator("//input[@name='contact_number']").fill("0359848555")

    # Select Gender
    page.locator("//select[@class='form-control select2-hidden-accessible']").select_option("Female")

    # Input Email
    page.get_by_role("textbox", name="Email").fill("liuduyquang@gmail.com")

    # Input Username
    page.get_by_role("textbox", name="Username").fill("LiuQuang")

    # Attach file
    page.locator("//input[@name='file' and contains(@class, 'custom-file-input')]").set_input_files("DuyQuang/BT_Buoi4/tests/uploadimg.png")

    # Click save button
    page.get_by_role("button", name="Save").click()



