from pathlib import Path
from playwright.sync_api import Page, expect
import random


def test_actions(page: Page):

    # Generate random data
    random_number = random.randint(1000, 9999)

    first_name = "Ngoc"
    last_name = "Do"
    password = "123456789"
    contact = "0900000001"
    email = f"abc{random_number}@test.com"
    username = f"UserNgocDo{random_number}"

    # File upload
    file_path = Path(__file__).parent / "filetest.jpg"

    # Open website
    page.goto("https://hrm.anhtester.com/")

    # Login
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")

    page.locator('//button[contains(@class,"btn-primary")]').click()

    # Open Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    page.get_by_role("link", name="Add New").click()

    # Fill form
    page.get_by_role("textbox", name="First Name").fill(first_name)

    page.get_by_role("textbox", name="Last Name").fill(last_name)

    page.get_by_role("textbox", name="password").fill(password)

    page.locator('//input[@name="contact_number"]').fill(contact)

    page.get_by_role("textbox", name="Email").fill(email)

    page.get_by_role("textbox", name="Username").fill(username)

    # Select gender
    page.locator('//select[@name="gender"]/following-sibling::span').click()
    page.locator('//li[normalize-space()="Female"]').click()

    # Upload file
    page.locator('//input[@name="file"]').set_input_files(str(file_path))

    # Save
    page.get_by_role("button", name="Save").click()

    # Wait table loaded
    page.wait_for_load_state("networkidle")

    # Search email
    page.locator('//input[@type="search"]').fill(email)

    # Wait search result
    page.wait_for_timeout(2000)

    # Name
    expect(page.locator("//tbody/tr/td[1]")).to_contain_text(f"{first_name} {last_name}")
    
    #Email
    expect(page.locator("//tbody/tr/td[1]")).to_contain_text(email)

    # Username
    expect(page.locator("//tbody/tr/td[2]")).to_have_text(username)

    # Contact
    expect(page.locator("//tbody/tr/td[3]")).to_have_text(contact)

    # Gender
    expect(page.locator("//tbody/tr/td[4]")).to_have_text("Female")

    # Status
    expect(page.locator("//tbody/tr/td[6]")).to_have_text("Active")

    print("SUCCESS")