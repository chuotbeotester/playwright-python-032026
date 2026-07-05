#1. Menu Manage Clients
#c1://a[contains(@href,'clients-list')]
#c2://*[@class = 'feather feather-user-check']/ancestor::a


#2. Button [+ Add New]
#c1://a[normalize-space()='Add New']
#c2://a[contains(@href, 'clients-grid')]/following-sibling::a


#3.1. Textbox:
# First Name *:
#c1://input[@name='first_name']
#c2://label[@for='company_name']/following-sibling::div//input

# Last Name *:
#c1://input[@name='last_name']
#c2://label[@for='last_name']/following-sibling::div//input

# Password *:
#c1://input[@name='password']
#c2://label[@for='website']/following-sibling::div//input

# Contact Number *:
#c1://input[@name='contact_number']
#c2://label[@for='contact_number']/following-sibling::input

# Email *:
#c1://input[@name='email']
#c2://label[@for='email']/following-sibling::div//input[@name='email']

# Username *:
#c1://input[@name='username']
#c2://label[@for='email']/following-sibling::div//input[@name='username']


#3.2. Dropdown list: Gender
#c1://select[@name='gender']
#c2://label[@for='gender']/following-sibling::select


#3.3. Button [Reset], button [Save]
# Button [Reset]
#c1://button[@type='reset']
#c2://button[@type = 'submit']/preceding-sibling::button[contains(text(), 'Reset')]

# Button [Save]
#c1://button[normalize-space() = 'Save']
#c2://button[@type='reset']/following-sibling::button


#3.4. Thẻ input trong trường Attachment
#c1://input[@type='file']
#c2://label[@class='custom-file-label']/preceding-sibling::input