'''
- Menu Magage Clients
    1.//a[@href='https://hrm.anhtester.com/erp/clients-list']
    2.//span[normalize-space()='Manage Clients']/parent::a

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
    1.//span[@role="combobox"]//span[@role="textbox"]
    2.//span[@class='select2-selection__arrow']/preceding-sibling::span

- Button: Reset
    1.//button[normalize-space()='Reset']
    2.//button[@type='submit']/preceding-sibling::button[normalize-space()='Reset']

- Button: Save
    1.//button[@type='reset']/following-sibling::button
    2.//div[@class='card-footer text-right']//button[@type='submit']

- Input
    1.//input[@name='file']
    2.//label[@class='custom-file-label']/preceding-sibling::input
'''