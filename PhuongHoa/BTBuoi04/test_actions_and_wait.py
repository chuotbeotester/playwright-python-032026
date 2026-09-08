from playwright.sync_api import Page

def test_actions(page: Page):
    
    #Login vao trang HRM
    page.goto('https://hrm.anhtester.com/')
    page.get_by_role('textbox', name='Your Username').fill('admin_example')
    page.get_by_role('textbox', name='Enter Password').fill('123456')
    page.locator('//button[@type="submit"]').click()

    #Vao trang Manage Clients va Add new client
    page.get_by_role('link', name="Manage Clients").click()
    page.locator('//a[normalize-space()="Add New"]').click()
    page.get_by_role('textbox', name='First Name').fill('Hoa')
    page.get_by_role('textbox', name='Last Name').fill('Nguyen')
    page.get_by_role('textbox', name='Password').fill('123456')
    page.locator('//input[@name="contact_number"]').fill('0966123456')
    page.locator('//select[@name="gender"]').select_option('Female')
    page.get_by_role('textbox', name='Email').fill('hoanp1@gmail.com')
    page.get_by_role('textbox', name='Username').fill('HoaNP1')
    page.locator('//input[@type="file"]').set_input_files('PhuongHoa/BTBuoi04/image.jpg')
    page.get_by_role("button", name="Save").click()