from playwright.sync_api import Page

def test_action(page: Page):
    #Login page
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button[contains(@class,  'btn-primar')]").click()
    
    #Click on Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    
    #Click on Add new button 
    page.get_by_role("link", name="Add New").click()
    
    # First Name field 
    page.get_by_role("textbox", name="First Name").fill("Ba")
    
    # Last name field
    page.get_by_role("textbox", name="Last Name").fill("Ngo Thi")
    
    # Password
    page.get_by_role("textbox", name="Password").fill("1234567")
    
    #Contact Number
    page.locator("//input[@name='contact_number']").fill("090807060504")
    
    # Gender
    page.locator("//select[@name='gender']").select_option("Female")
    
    #Email
    page.get_by_role("textbox", name="Email").fill("a@gmail.com")
    
    #Username
    page.get_by_role("textbox", name="Username").fill("Ba052126")
    
    #Choose File
    page.locator("//input[@type='file']").set_input_files("tests/download.jpg")
  
    #Click on Save button
    page.get_by_role("button", name="Save").click()
    

