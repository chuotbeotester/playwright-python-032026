from playwright.sync_api import Page, expect

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
    page.get_by_role("textbox", name="Email").fill("a1@gmail.com")
    
    #Username
    page.get_by_role("textbox", name="Username").fill("Ba0521260")
    
    #Choose File
    page.locator("//input[@type='file']").set_input_files("download.jpg")
  
    #Click on Save button
    page.get_by_role("button", name="Save").click()
    
    
   # Search box
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible() # type: ignore
    page.get_by_role("searchbox", name="Search").fill("a1@gmail.com")  # type: ignore
   
   #Check Name, Email 
    expect(page.locator("//h6[contains(text(),'Ba Ngo Thi')]")).to_contain_text("Ba Ngo Thi")
   
    expect(page.locator("//p[contains(text(),'a1@gmail.com')]")).to_contain_text("a1@gmail.com") # type: ignore
   
   #Check Username
    expect(page.locator("//td[normalize-space()='Ba0521260']")).to_contain_text("Ba0521260") # type: ignore
   
   #Check Contact Number
    expect(page.locator("//*[@id='xin_table']/tbody/tr[1]/td[3]")).to_have_text("090807060504") # type: ignore
   
   #Check Gender
    expect(page.locator("//*[@id='xin_table']/tbody/tr[1]/td[4]")).to_have_text("Female") # type: ignore
   
   #Check Status
    expect(page.locator("//table[@id='xin_table']/tbody/tr[1]/td[6]")).to_have_text("Active") # type: ignore