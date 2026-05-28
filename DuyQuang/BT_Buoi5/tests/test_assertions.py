import re
from playwright.sync_api import Playwright, Page, sync_playwright, expect
import time

def test_add_user(page : Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//i[@class='fas fa-user-lock d-blockd']").click()
    # time.sleep(5)

    page.get_by_role("link", name="Manage Clients").click()
    # page.get_by_role("link", name="Add New").click()
    # page.get_by_role("textbox", name="First Name").fill("Liu")
    # page.get_by_role("textbox", name="Last Name").fill("Quang")
    # page.get_by_role("textbox", name="Password").fill("123456")
    # page.locator("//input[@name='contact_number']").fill("0359848555")
    # page.locator("//select[@class='form-control select2-hidden-accessible']").select_option("Female")
    # page.get_by_role("textbox", name="Email").fill("liuduyquang@gmail.com")
    # page.get_by_role("textbox", name="Username").fill("LiuQuang")
    # page.locator("//input[@name='file' and contains(@class, 'custom-file-input')]").set_input_files("tests/uploadimg.png")
    # page.get_by_role("button", name="Save").click()
    page.get_by_role("searchbox", name="Search").fill("liuduyquang@gmail.com")
    time.sleep(5)
    expect(page.locator("//h6[@class='m-b-0']")).to_contain_text("Liu Quang")
    expect(page.locator("//p[@class='m-b-0']")).to_contain_text("liuduyquang@gmail.com")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[1]")).to_contain_text("LiuQuang")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[2]")).to_contain_text("0359848555")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[3]")).to_contain_text("Female")
    expect(page.locator("//span[@class='badge badge-light-success']")).to_contain_text("Active")

   






