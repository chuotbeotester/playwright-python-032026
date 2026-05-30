from playwright.sync_api import Page, expect
import time, re
first_name="Minh"
last_name="Tue3"
password="123456"
contact="0357217333"
email="dominhtue5555@gmail.com"
username="dominhtue5555"

def test_add_new_client(page: Page):
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role ("textbox", name="Your Username").click()

    page.get_by_role ("textbox", name="Your Username").fill("admin_example")
    page.get_by_role ("textbox", name="Enter Password").click()
    
    page.get_by_role ("textbox", name="Enter Password").fill("123456")
    btn_login = page.locator("//button[contains(@class,'btn-primary')]")
    btn_login.click()
  
    # Click menu "Manage Clients"
    menu_manage_clients = page.locator("//a[normalize-space()='Manage Clients']")
    menu_manage_clients.click()
    # Click button [+ Add New]
    btn_add_new = page.locator("//a[normalize-space()='Add New']")
    btn_add_new.click()
    
    # # Fill in the form
    page.locator("//input[@name='first_name']").fill(first_name)
    
    page.locator("//input[@name='last_name']").fill(last_name)
    
    page.locator("//input[@name='password']").fill(password)
    
    page.locator("//input[@name='contact_number']").fill(contact)
    
    page.locator("//input[@name='email']").fill(email)
 
    page.locator("//input[@name='username']").fill(username)
  
    gender_dropdown = page.locator("//select[@name='gender']")
    gender_dropdown.select_option("Male")
    
    # #input file
    page.locator("//input[@type='file']").set_input_files("avatar-vo-tri-nam-2.jpg")
   
    # # Click button [Save]
    btn_save = page.locator("//button[normalize-space()='Save']")
    btn_save.click()
    
    # Nhập Email đã tạo vào Textbox Search
    page.get_by_role("searchbox", name="Search").fill(email)
    # Kiểm tra kết quả trả về có đúng Email đã tạo hay không
    expect(page.locator("//h6[@class='m-b-0']")).to_contain_text(f"{first_name} {last_name}")
    expect(page.locator("//p[@class='m-b-0']")).to_contain_text(email)
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[1]")).to_contain_text(username)
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[2]")).to_contain_text(contact)
    expect(page.locator("//div[@class='d-inline-block align-middle']/following::td[3]")).to_contain_text("Male")
    expect(page.locator("//span[@class='badge badge-light-success']")).to_contain_text("Active")