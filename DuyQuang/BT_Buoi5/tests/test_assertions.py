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

    # Search for user by email
    page.get_by_role("searchbox", name="Search").fill("liuduyquang@gmail.com")

    # Verify search results
    expect(page.locator("//h6[@class='m-b-0']")).to_contain_text("Liu Quang")
    expect(page.locator("//p[@class='m-b-0']")).to_contain_text("liuduyquang@gmail.com")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[1]")).to_contain_text("LiuQuang")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[2]")).to_contain_text("0359848555")
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[3]")).to_contain_text("Female")
    expect(page.locator("//span[@class='badge badge-light-success']")).to_contain_text("Active")

   






