from playwright.sync_api import Page, expect
from pathlib import Path


def test_bai_tap_buoi_5(page:Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_placeholder("Your Username").fill("admin_example")
    page.get_by_placeholder("Enter Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    page.get_by_role("link", name="Manage Clients").click()
    page.get_by_role("link", name="Add New").click()
    page.get_by_placeholder("First Name").fill("GMO")
    page.get_by_placeholder("Last Name").fill("Testing")
    page.get_by_placeholder("Password").fill("123456") 
    page.get_by_placeholder("Contact Number").fill("0123456789")
    dropdown = page.locator("//span[@role = 'combobox']")
    dropdown.locator("//span[@role = 'textbox']").click()
    dropdown.get_by_text("Male").click()
    page.get_by_placeholder("Email").fill("gmo@gmail.com")
    page.get_by_placeholder("Username").fill("Ka Li Test")
    page.get_by_role("button", name="Choose File") \
        .set_input_files(Path(__file__).parent / "demo_example_2.jpg")
    page.get_by_role("button", name="Save").click()
    expect(page.locator("#xin_table")).to_contain_text("GMO Testing")
    page.get_by_role("searchbox", name="Search").fill("gmo@gmail.com")
    expect(page.locator("//td[@class='sorting_1']//div[@class='d-inline-block']//h6[@class='m-b-0']")).to_have_text("GMO Testing")
    expect(page.locator("//td[@class='sorting_1']//div[@class='d-inline-block']//p[@class='m-b-0']")).to_have_text("gmo@gmail.com")
    expect(page.locator("//table//tbody/tr/td[2]")).to_have_text("Ka Li Test")
    expect(page.locator("//table//tbody/tr/td[3]")).to_have_text("0123456789")
    expect(page.locator("//table//tbody/tr/td[4]")).to_have_text("Male")
    expect(page.locator("//table//tbody/tr/td[6]")).to_have_text("Active")