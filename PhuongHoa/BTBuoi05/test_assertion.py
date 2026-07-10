from playwright.sync_api import Page, expect

def test_assertion(page: Page):
    
    #Login vao trang HRM - Arrange
    page.goto('https://hrm.anhtester.com/')
    page.get_by_role('textbox', name='Your Username').fill('admin_example')
    page.get_by_role('textbox', name='Enter Password').fill('123456')
    page.locator('//button[@type="submit"]').click()

    #Vao trang Manage Clients - Arrange
    page.get_by_role('link', name="Manage Clients").click()

    #Add new client - Action
    page.locator('//a[normalize-space()="Add New"]').click()
    page.get_by_role('textbox', name='First Name').fill('Hoa')
    page.get_by_role('textbox', name='Last Name').fill('Nguyen')
    page.get_by_role('textbox', name='Password').fill('123456')
    page.locator('//input[@name="contact_number"]').fill('0966123456')
    page.locator('//select[@name="gender"]').select_option('Female')
    page.get_by_role('textbox', name='Email').fill('hoanp2@gmail.com')
    page.get_by_role('textbox', name='Username').fill('HoaNP2')
    page.locator('//input[@type="file"]').set_input_files('PhuongHoa/BTBuoi05/image.jpg')
    page.get_by_role("button", name="Save").click()

    #Search new client - Action
    page.get_by_role('searchbox', name='Search').fill('hoanp2@gmail.com')

    #Assertion
    #Name
    Name = page.locator('//table[@id="xin_table"]//td[1]')
    expect(Name).to_contain_text("Hoa Nguyen")
    expect(Name).to_contain_text("hoanp2@gmail.com")

    #Username
    Username = page.locator('//table[@id="xin_table"]//td[2]')
    expect(Username).to_contain_text("HoaNP2")

    #ContactNumber
    ContactNumber = page.locator('//table[@id="xin_table"]//td[3]')
    expect(ContactNumber).to_contain_text("0966123456")

    #Gender
    Gender = page.locator('//table[@id="xin_table"]//td[4]')
    expect(Gender).to_contain_text("Female")

    #Status
    Status = page.locator('//table[@id="xin_table"]//td[6]')
    expect(Status).to_contain_text("Active")