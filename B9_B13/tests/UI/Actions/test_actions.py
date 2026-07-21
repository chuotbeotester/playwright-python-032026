from playwright.sync_api import Page, expect
import time, re

def test_actions(page: Page):
    
    page.goto("https://hrm.anhtester.com/")
    
    expect(page).to_have_title("HRM | Anh Tester Demo | Log in")
    expect(page).to_have_url(re.compile("hrm.anhtester.com"))

    # title = page.locator("//h4")
    # expect(title).to_contain_text("Welcome to HRM | Anh Tester Demo ")

    expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    txtUsername = page.get_by_role("textbox", name="Your Username")
    expect(txtUsername).to_have_attribute("placeholder", "Your Username")

    page.get_by_role("textbox", name="Your Username").fill("admin_example")

    # page.get_by_role("textbox", name="Enter Password").fill("123456")
    # page.locator("//button/span[normalize-space()='Login']").click()

    # logo = page.locator("//div[@class='page-header']//img")
    # expect(logo).to_have_attribute("src", "https://hrm.anhtester.com/public/uploads/users/thumb/test111.jpg")
    # # page.get_by_role("link", name="Employees").click() 
    # # page.get_by_role("link", name=" Add New").click()

    # time.sleep(3)
    # expect(page.locator('//span[contains(@id,"select2-designation")]')).to_be_disabled()

    # page.locator("#department_id").select_option(label="QA")
    # time.sleep(3)

    # expect(page.locator('//span[contains(@id,"select2-designation")]')).to_be_enabled()
    # page.locator('//select[@name="designation_id"]').select_option("9")
























    # page.locator('//button[contains(@class, "btn-primary")]').wait_for(timeout=600000)


    # page.get_by_role("textbox", name="Your Username").dblclick()
    # time.sleep(5)
    # page.wait_for_timeout(5000)

    # page.get_by_role("textbox", name="Your Username").press("Delete")

    # print("Open Core HR menu")
    # page.get_by_role("link", name ="Core HR").click()
    # page.get_by_role("link", name ="Policies").click()
    # time.sleep(3)
    # page.get_by_role("combobox", name ="Show entries").select_option(index=3)
    # time.sleep(5)

    # page.locator("#attachment").set_input_files("tests/fileupload.png")
    # page.locator('//a[@data-toggle="tooltip"]//*[@class="feather feather-user-check"]').click()
    
    # page.locator("//i[@data-toggle='tooltip']").hover()
    # time.sleep(5)
   

    