from playwright.sync_api import Page, expect 
import time 

first_name = "Trang4"
last_name = "Nguyen"
pass_word = "123456@"
email = "trang6@gmail.com"
user_name = "Huyentrang6"
contact_number = "0666666666"
gender = "Male"

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
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").fill(last_name)
    page.get_by_role("textbox", name="Password").fill(pass_word)
    page.get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Username").fill(user_name)
    page.locator('input[name="contact_number"]').fill(contact_number)
    page.locator('//label[normalize-space()="Gender"]/following-sibling::select').select_option(label=gender)
    page.locator("//input[@type='file']").set_input_files("Huyen_Trang/BTBuoi5/tests/image.jpg")
    
    page.get_by_role("button", name="Save").click()

    #Search email
    page.get_by_role("searchbox", name="Search").fill(email)
    time.sleep(3)

    #Check info in table 
    expect(page.locator('//h6[@class="m-b-0"]')).to_have_text(first_name+" "+last_name)
    expect(page.locator('//p[@class="m-b-0"]')).to_have_text(email)
    expect(page.locator("//tbody/tr[1]/td[2]")).to_have_text(user_name)
    expect(page.locator("//tbody/tr[1]/td[3]")).to_have_text(contact_number)
    expect(page.locator("//tbody/tr[1]/td[4]")).to_have_text(gender)
    expect(page.locator("//tbody/tr[1]/td[6]")).to_have_text("Active")

    time.sleep(3)


    
