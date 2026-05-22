'''
- Menu Magage Clients
    1.//span[normalize-space()='Manage Clients']
    2.(//a[@class='pc-link '])[8]/span[@class='pc-mtext']

- Button [+ Add New]
    1.//a[normalize-space()='Add New']
    2.//*[name()='svg' and contains(@class,'feather feather-plus')]/parent::a

- Textbox: First Name
    1.//input[@name='first_name']
    2.//label[@for='company_name']/following-sibling::div/input
- Textbox: Last Name
    1.//input[@name='last_name']
    2.//label[@class='control-label']/following-sibling::div//input
- Textbox: Password
    1.//input[@name='password']
    2.(//div[@class='input-group-prepend'])[3]/following-sibling::input
- Textbox: Contact Number
    1.//input[@placeholder='Contact Number']
    2.//label[@for='contact_number']/following-sibling::input
- Textbox: Email
    1. //input[@placeholder='Email']
    2.//label[contains(text(),'Email')]/following-sibling::div/input
- Textbox: Username
    1.//input[@placeholder='Username']
    2.//label[contains(text(),'Username')]/following-sibling::div/input
- Dropdown list: Gender 
    1.//span[@id='select2-gender-5z-container']
    2.//span[@class='selection']//span[@role='textbox']
- Button: Reset
    1.//button[normalize-space()='Reset']
    2.//div[@class='card-footer text-right']//button[@type='reset']
- Button: Save
    1.//span[normalize-space()='Save']
    2.//div[@class='card-footer text-right']//button[@type='submit']
- Input
    1.//input[@name='file']
    2.//div[@class='custom-file']//input
'''