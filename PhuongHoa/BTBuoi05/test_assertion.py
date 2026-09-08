from playwright.sync_api import Page, expect

def test_assertion(page: Page):
    
    #Login vao trang HRM - Arrange
    url = 'https://hrm.anhtester.com/'
    username = 'admin_example'
    password = '123456'

    page.goto(url)
    page.get_by_role('textbox', name='Your Username').fill(username)
    page.get_by_role('textbox', name='Enter Password').fill(password)
    page.locator('//button[@type="submit"]').click()

    #Vao trang Manage Clients - Arrange
    page.get_by_role('link', name="Manage Clients").click()

    #Add new client - Action
    firstname = 'Hoa'
    lastname = 'Nguyen'
    password_user = '123456'
    contact_number = '0966123456'
    gender = 'Female'
    email = 'hoanp2@gmail.com'
    user = 'HoaNP2'
    file_path = 'PhuongHoa/BTBuoi05/image.jpg'
    status_user = 'Active'

    page.locator('//a[normalize-space()="Add New"]').click()
    page.get_by_role('textbox', name='First Name').fill(firstname)
    page.get_by_role('textbox', name='Last Name').fill(lastname)
    page.get_by_role('textbox', name='Password').fill(password_user)
    page.locator('//input[@name="contact_number"]').fill(contact_number)
    page.locator('//select[@name="gender"]').select_option(gender)
    page.get_by_role('textbox', name='Email').fill(email)
    page.get_by_role('textbox', name='Username').fill(user)
    page.locator('//input[@type="file"]').set_input_files(file_path)
    page.get_by_role("button", name="Save").click()

    #Search new client - Action
    page.get_by_role('searchbox', name='Search').fill(email)

    #Assertion
    #Name
    Name = page.locator('//table[@id="xin_table"]//td[1]')
    full_name = [firstname, lastname]
    expect(Name).to_contain_text("".join(full_name))
    expect(Name).to_contain_text(email)

    #Username
    Username = page.locator('//table[@id="xin_table"]//td[2]')
    expect(Username).to_contain_text(user)

    #ContactNumber
    ContactNumber = page.locator('//table[@id="xin_table"]//td[3]')
    expect(ContactNumber).to_contain_text(contact_number)

    #Gender
    Gender = page.locator('//table[@id="xin_table"]//td[4]')
    expect(Gender).to_contain_text(gender)

    #Status
    Status = page.locator('//table[@id="xin_table"]//td[6]')
    expect(Status).to_contain_text(status_user)