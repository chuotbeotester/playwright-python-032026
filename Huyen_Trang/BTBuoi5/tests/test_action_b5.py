from playwright.sync_api import Page, expect 
import time 

def test_action(page: Page):
    page.goto("https://hrm.anhtester.com/")

    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button[contains(@class, 'btn-primary')]").click()

    
    #Click on Manage Clients
    page.get_by_role("link", name="Manage Clients").click()

    #Click on Add new button
    page.get_by_role("link", name="Add New").click()

    #Fill fields and save 
    page.get_by_role("textbox", name="First Name").fill("Trang4")
    page.get_by_role("textbox", name="Last Name").fill("Nguyen")
    page.get_by_role("textbox", name="Password").fill("123456@")
    page.get_by_role("textbox", name="Email").fill("trang4@gmail.com")
    page.get_by_role("textbox", name="Username").fill("Huyentrang4")
    page.locator('input[name="contact_number"]').fill("0666666666")
    page.locator('//label[normalize-space()="Gender"]/following-sibling::select').select_option(label="Female")
    page.get_by_role("button", name="Choose File").set_input_files("tests/image.jpg")
    
    page.get_by_role("button", name="Save").click()

    #Search email
    page.get_by_role("searchbox", name="Search").fill("trang4@gmail.com")
    time.sleep(3)

    #Check info in table 
    expect(page.locator('//h6[@class="m-b-0"]')).to_have_text("Trang4 Nguyen")
    expect(page.locator('//p[@class="m-b-0"]')).to_have_text("trang4@gmail.com")
    expect(page.get_by_role("gridcell", name="Huyentrang4")).to_have_text("Huyentrang4")
    expect(page.get_by_role("gridcell", name="0666666666")).to_have_text("0666666666")
    expect(page.get_by_role("gridcell", name="Female")).to_have_text("Female")
    expect(page.get_by_role("gridcell", name="Active")).to_have_text("Active")

    time.sleep(3)


    
