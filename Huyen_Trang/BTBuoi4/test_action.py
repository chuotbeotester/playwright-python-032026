from playwright.sync_api import Page
import time 

def test_action(page: Page):
    page.goto("https://hrm.anhtester.com/")

    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button[contains(@class, 'btn-primary')]").click()

    

    page.get_by_role("link", name="Manage Clients").click()
    page.get_by_role("link", name="Add New").click()

    page.get_by_role("textbox", name="First Name").fill("Trang")
    page.get_by_role("textbox", name="Last Name").fill("Nguyen")
    page.get_by_role("textbox", name="Password").fill("123456@")
    page.get_by_role("textbox", name="Email").fill("trang@gmail.com")
    page.get_by_role("textbox", name="Username").fill("Huyentrang")
    page.locator('input[name="contact_number"]').fill("01234567891")
    page.locator('//label[normalize-space()="Gender"]/following-sibling::select').select_option(label="Female")
    page.get_by_role("button", name="Choose File").set_input_files("BTBuoi4/image.jpg")
    
    page.get_by_role("button", name="Save").click()
    time.sleep(5)
    



    




