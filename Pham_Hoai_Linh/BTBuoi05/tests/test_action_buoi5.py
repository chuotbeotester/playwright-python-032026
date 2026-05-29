from playwright.sync_api import Page, expect
import time
 

def test_actions_buoi5(page: Page):

    # ARRANGE
    page.goto("https://hrm.anhtester.com/")
    
    firstName = "Pham"
    lastName = "Linh"
    password = "112233"
    contactNumber = "0123345577"
    email = "linh.pham+4@gmail.com"
    userName = "linhpham#4"
    gender = "Male"
    
    # ACTION
    
    # Login process
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[@class="btn btn-primary mt-2 ladda-button"]').click()
    
    # Click on the Manage Client left-menu
    page.get_by_role("link", name="Manage Clients").click()
    
    # Click on the Add New button
    page.get_by_role("link", name="Add New").click()
    
    # Input First Name
    page.get_by_role("textbox", name="First Name").fill(firstName)
    
    # Input Last Name
    page.get_by_role("textbox", name="Last Name").fill(lastName)
    
    # Input Password
    page.get_by_role("textbox", name="Password").fill(password)
    
    # Input Contact Number (phone numer)
    page.locator('//input[@name="contact_number"]').fill(contactNumber)
    
    # Input Email
    page.get_by_role("textbox", name="Email").fill(email )
    
    # Input User Name
    page.get_by_role("textbox", name="Username").fill(userName)
    
    # Select gender
    page.locator('//select[@class="form-control select2-hidden-accessible"]').select_option(label=gender)
    
    # Upload file
    page.locator('//input[@class="custom-file-input"]').set_input_files("Pham_Hoai_Linh/BTBuoi05/tests/avatar.png")
    
    # Click on the Save button
    page.get_by_role("button", name="Save").click()
    
    # Input email to search
    page.get_by_role("searchbox", name="Search").fill(email)
    
    
    # ASSERT
    
    # Verify Name
    expect(page.locator('//h6[@class="m-b-0"]')).to_have_text(firstName+" "+lastName)
    
    #Verify email
    expect(page.locator('//p[@class="m-b-0"]')).to_have_text(email)
    
    # Verify User name
    expect(page.get_by_role("gridcell", name = userName)).to_have_text(userName)
    
    # Verify Contact number
    expect(page.get_by_role("gridcell", name = contactNumber)).to_have_text(contactNumber)
    
    # Verify Gender
    expect(page.get_by_role("gridcell", name = gender)).to_have_text(gender)
    
    # Verify Status
    expect(page.get_by_role("gridcell", name = "Active")).to_have_text("Active")
    