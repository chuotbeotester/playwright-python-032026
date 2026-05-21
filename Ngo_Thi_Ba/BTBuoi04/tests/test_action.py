from playwright.sync_api import Page
import time

def action(page: Page):
    #Login page
    page.goto("Truy cập trang: https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").click()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Your Username").press("Tab")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.get_by_role("textbox", name="Enter Password").press("Enter")
    page.get_by_role("button", name=" Login").click()
    time.sleep(5)
    
    #Click on Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    #Click on Add new button 
    page.get_by_role("link", name="Add New").click()
    # First Name field 
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("Ngo Thi")
    page.get_by_role("textbox", name="First Name").press("Tab")
    # Last name field
    page.get_by_role("textbox", name="Last Name").fill("Ba")
    page.get_by_role("textbox", name="Last Name").press("Tab")
    # Password
    page.get_by_role("textbox", name="Password").fill("1234567")
    page.get_by_role("textbox", name="Password").press("Tab")
    #Contact Number
    page.get_by_placeholder("Contact Number").fill("090807060504")
    page.get_by_placeholder("Contact Number").press("Tab")
    # Gender
    page.get_by_role("option", name="Female").click()
    #Email
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("a@gmail.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    #Username
    page.get_by_role("textbox", name="Username").fill("Ba052126")
    #Choose File
    page.get_by_role("button", name="Choose File").click()
    page.get_by_role("button", name="Choose File").set_input_files("Screenshot 2026-04-01 153256.png")
    time.sleep(5)
    
    #Click on Save button
    page.get_by_role("button", name="Save").click()
    time.sleep(3)