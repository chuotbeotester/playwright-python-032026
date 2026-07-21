from playwright.sync_api import Page, expect
import time, re

def test_actions(page: Page):
    
    page.goto("https://hrm.anhtester.com/")
    
    # expect(page).to_have_title("HRM | Anh Tester Demo | Log in")
    # expect(page).to_have_url(re.compile("hrm.anhtester.com"))

    # expect(page.get_by_role("textbox", name="Your Username")).to_be_visible()
    # txtUsername = page.get_by_role("textbox", name="Your Username")
    # # expect(txtUsername).to_have_attribute("placeholder", "Your Username")

    # page.get_by_role("textbox", name="Your Username").fill("admin_example")

    # page.get_by_role("textbox", name="Enter Password").fill("123456")

    expect(page.locator("//div[@class='toast-message']")).to_be_visible()
    try:
        pass
    except:
        pass

    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button/span[normalize-space()='Login']").click()
  


    # page.locator("//span[normalize-space()='Projects']/parent::a").click()
    # page.locator("//select[@name='xin_table_length']").select_option("25")
    # time.sleep(2)
    # countProjects = page.locator("//table[@id='xin_table']/tbody/tr")

    # expect(countProjects).to_have_count(25)
