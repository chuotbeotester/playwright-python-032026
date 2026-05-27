from playwright.sync_api import Page, expect
import time
 

def test_actions_buoi5(page: Page):

    # ARRANGE
    page.goto("https://hrm.anhtester.com/")
    
    # ACTION
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[@class="btn btn-primary mt-2 ladda-button"]').click()
    page.get_by_role("link", name="Manage Clients").click()
    # page.get_by_role("link", name="Add New").click()
    # page.get_by_role("textbox", name="First Name").fill("Pham")
    # page.get_by_role("textbox", name="Last Name").fill("Linh")
    # page.get_by_role("textbox", name="Password").fill("112233")
    # page.locator('//input[@name="contact_number"]').fill("0123321789")
    # page.get_by_role("textbox", name="Email").fill("linh.pt.kh@gmail.com")
    # page.get_by_role("textbox", name="Username").fill("linhpham")
    # page.locator('//select[@class="form-control select2-hidden-accessible"]').select_option(label="Male")
    # page.locator('//input[@class="custom-file-input"]').set_input_files("Pham_Hoai_Linh/BTBuoi05/tests/avatar.png")
    # page.get_by_role("button", name="Save").click()
    
    page.get_by_role("searchbox", name="Search").fill("linh.pt.kh@gmail.com")
    
    time.sleep(2)
    
    # ASSERT
    expect(page.locator('//h6[@class="m-b-0"]')).to_have_text("Pham Linh")
    expect(page.locator('//p[@class="m-b-0"]')).to_have_text("linh.pt.kh@gmail.com")
    expect(page.get_by_role("gridcell", name = "linhpham")).to_have_text("linhpham")
    expect(page.get_by_role("gridcell", name = "0123321789")).to_have_text("0123321789")
    expect(page.get_by_role("gridcell", name = "Male")).to_have_text("Male")
    expect(page.get_by_role("gridcell", name = "Active")).to_have_text("Active")
    