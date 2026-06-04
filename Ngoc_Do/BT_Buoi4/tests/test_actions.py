from playwright.sync_api import Page  
import time

def test_actions(page: Page):
    page.goto("https://hrm.anhtester.com/")

    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")

    btn_login = page.locator('//button[contains(@class,"btn-primary")]')
    btn_login.click()

    print("Open Manage Clients")
    page.get_by_role("link", name="Manage Clients").click()
    page.get_by_role("link", name="Add New").click()

    page.get_by_role("textbox", name="First Name").fill("Ngoc")
    page.get_by_role("textbox", name="Last Name").fill("Do")
    page.get_by_role("textbox", name="password").fill("123456789")
    contact_number = page.locator('//input[@name="contact_number"]')
    contact_number.fill("0900000001")
    page.get_by_role("textbox", name="Email").fill("ngocdo@example.com")
    page.get_by_role("textbox", name="Username").fill("UserNgocDo")
    page.click('//select[@name="gender"]/following-sibling::span')
    page.click('//li[normalize-space()="Female"]')
    btn_attachment = page.locator('//input[@name="file"]')
    btn_attachment.set_input_files("tests/travel_image.jpeg")

    page.get_by_role("button", name="Save").click()
    time.sleep(5)



