#Menu Manage Clients1: //span[normalize-space()='Manage Clients']
#Menu Manage Clients2: //span[normalize-space()='Manage Clients']/ancestor::a

#Button +Add New1: //a[normalize-space()='Add New']
#Button +Add New2: //div[@id='xin_table_wrapper']//ancestor::div//a[normalize-space()='Add New']

#Textbox Frist Name1: //input[@name='first_name']
#Textbox Frist Name2: //label[contains(.,'First Name')]/following-sibling::div//input

#Textbox Last Name1: //input[@name='last_name']
#Textbox Last Name2: //label[contains(.,'Last Name')]/following-sibling::div//input

#Textbox Password1: //input[@name='password']
#Textbox Password2: //label[contains(.,'Password')]/following-sibling::div//input

#Textbox Contact Number1: //input[@name='contact_number']
#Textbox Contact Number2: //label[contains(.,'Contact Number')]/following-sibling::input

#Textbox Email1: //input[@name='email']
#Textbox Email2: //label[contains(.,'Email')]/following-sibling::div//input

#Textbox Username1: //input[@name='username']
#Textbox Username2: //label[contains(.,'Username')]/following-sibling::div//input

#Dropdown list Gender1: //select[@name='gender']
#Dropdown list Gender2: //label[contains(.,'Gender')]/following-sibling::span

#Button Reset1: //button[@type='reset']
#Button Reset2: //button[@type='submit']/preceding-sibling::button[normalize-space()='Reset']

#Button Save1: //button[@type='submit']
#Button Save2: //button[@type='reset']/following-sibling::button//span[normalize-space()='Save']

#Input Attachment1: //input[@type='file']
#Input Attachment2: //label[@for='logo']/following-sibling::div//input[@type='file']