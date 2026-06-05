from playwright.sync_api import Page, expect

def test_action(page: Page):
    
    firstName = 'Ba'
    lastName = 'Ngo Thi'
    password = '1234567'
    contactNumber = '090807060504'
    email = 'a1@gmail.com'
    userName = 'Ba0521260'
    gender = 'Female'
    
    
    #Login page
    page.goto("https://hrm.anhtester.com/")
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator("//button[contains(@class,  'btn-primar')]").click()
    
    #Click on Manage Clients
    page.get_by_role("link", name="Manage Clients").click()
    
    #Click on Add new button 
    page.get_by_role("link", name="Add New").click()
    
    # Fill first Name 
    page.get_by_role("textbox", name="First Name").fill(firstName)
    
    # Fill last name field
    page.get_by_role("textbox", name="Last Name").fill(lastName)
    
    # Fill password
    page.get_by_role("textbox", name="Password").fill(password)
    
    #Fill Contact Number
    page.locator("//input[@name='contact_number']").fill(contactNumber)
    
    # Select Gender
    page.locator("//select[@name='gender']").select_option(gender)
    
    #Fill Email
    page.get_by_role("textbox", name="Email").fill(email)
    
    #Fill Username
    page.get_by_role("textbox", name="Username").fill(userName)
    
    #Choose File
    page.locator("//input[@type='file']").set_input_files("Ngo_Thi_Ba/BTBuoi05/tests/download.jpg")
  
    #Click on Save button
    page.get_by_role("button", name="Save").click()
    
    
   #Check search box
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible() # type: ignore
    page.get_by_role("searchbox", name="Search").fill("a1@gmail.com")  # type: ignore
   
   #Check Name, Email 
    expect(page.locator('//*[@id="xin_table"]/tbody/tr[1]/td[1]')).to_contain_text(firstName +" "+lastName)
   
    expect(page.locator("//tbody/tr/td[1]")).to_contain_text(email) # type: ignore
   
   #Check Username
    expect(page.locator("//tbody/tr/td[2]")).to_contain_text(userName) # type: ignore
   
   #Check Contact Number
    expect(page.locator("//*[@id='xin_table']/tbody/tr[1]/td[3]")).to_have_text(contactNumber) # type: ignore
   
   #Check Gender
    expect(page.locator("//*[@id='xin_table']/tbody/tr[1]/td[4]")).to_have_text(gender) # type: ignore
   
   #Check Status
    expect(page.locator("//*[@id='xin_table']/tbody/tr[1]/td[6]")).to_have_text("Active") # type: ignore