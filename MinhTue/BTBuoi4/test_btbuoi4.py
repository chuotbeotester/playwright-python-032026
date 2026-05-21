from playwright.sync_api import Page, expect
import time, re
def test_add_new_client(page: Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role ("textbox", name="Your Username").click()
    time.sleep(3)
    page.get_by_role ("textbox", name="Your Username").fill("admin_example")
    page.get_by_role ("textbox", name="Enter Password").click()
    time.sleep(3)
    page.get_by_role ("textbox", name="Enter Password").fill("123456")
    btn_login = page.locator("//button[contains(@class,'btn-primary')]")
    btn_login.click()
    time.sleep(3)
    # Click menu "Manage Clients"
    menu_manage_clients = page.locator("//a[normalize-space()='Manage Clients']")
    menu_manage_clients.click()
    time.sleep(3)
    # Click button [+ Add New]
    btn_add_new = page.locator("//a[normalize-space()='Add New']")
    btn_add_new.click()
    time.sleep(3)
    # Fill in the form
    page.locator("//input[@name='first_name']").fill("Minh")
    time.sleep(1)
    page.locator("//input[@name='last_name']").fill("Tue")
    time.sleep(1)
    page.locator("//input[@name='password']").fill("123456")
    time.sleep(1)
    page.locator("//input[@name='contact_number']").fill("0343250620")
    time.sleep(1)
    page.locator("//input[@name='email']").fill("dominhtue.qa@gmail.com")
    time.sleep(1)
    page.locator("//input[@name='username']").fill("dominhtue")
    time.sleep(1)
    gender_dropdown = page.locator("//select[@name='gender']")
    gender_dropdown.select_option("Male")
    time.sleep(1)
    #input file
    page.set_input_files("//input[@type='file']", "D:\\PYTHON_MINHTUE\\tests\\avatar-vo-tri-nam-2.jpg")
    time.sleep(5)
    # Click button [Save]
    btn_save = page.locator("//button[normalize-space()='Save']")
    btn_save.click()
    time.sleep(3)
