from playwright.sync_api import Page
import time

def test_actions(page: Page):

    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[@class="btn btn-primary mt-2 ladda-button"]').click()
    page.get_by_role("link", name="Manage Clients").click()
    page.get_by_role("link", name="Add New").click()
    page.get_by_role("textbox", name="First Name").fill("Pham")
    page.get_by_role("textbox", name="Last Name").fill("Linh")
    page.get_by_role("textbox", name="Password").fill("112233")
    page.locator('//input[@name="contact_number"]').fill("0123321789")
    page.get_by_role("textbox", name="Email").fill("linh.pt.kh@gmail.com")
    page.get_by_role("textbox", name="Username").fill("linhpham")
    page.locator('//select[@class="form-control select2-hidden-accessible"]').select_option(label="Male")
    page.locator('//input[@class="custom-file-input"]').set_input_files("avatar.png")
    page.get_by_role("button", name="Save").click()

    time.sleep(10)