from playwright.sync_api import Page
import time

def test_actions_BTBuoi4(page:Page):
    print("Start open URL")
    page.goto("https://hrm.anhtester.com/erp/login")
    page.get_by_role('textbox', name='Your Username').fill("admin_example")
    page.get_by_role('textbox', name='Enter Password').fill("123456")
    page.locator('//button[contains(@class,"btn-primary")]').click()
    time.sleep(5)

    print("Click menu ManageClients")
    page.locator('//span[normalize-space()="Manage Clients"]').click()
    page.locator('//a[normalize-space()="Add New"]').click()
    time.sleep(5)

    print("Fill information")
    page.get_by_role('textbox', name='First Name').fill("ThanhHuy")
    page.get_by_role('textbox', name='Last Name').fill("Nguyen")
    page.get_by_role('textbox', name='Password').fill("123456")
    page.locator('//input[@placeholder="Contact Number"]').fill("0987654321")
    page.get_by_role('textbox', name='Email').fill("ngthhuy98@gmail.com")
    page.get_by_role('textbox', name='Username').fill("ngthhuy98")
    page.locator('//select[@name="gender"]').select_option("Male")
    page.locator('//input[@name="file"]').set_input_files("ThanhHuy/BTBuoi04/data/attached_file.png")
    page.locator('//span[normalize-space()="Save"]').click()
    time.sleep(5)
