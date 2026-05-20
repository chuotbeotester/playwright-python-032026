# https://hrm.anhtester.com/erp/clients-list
# Manage Clients
# //a[normalize-space()='Manage Clients']
# //span[normalize-space()='Manage Clients']/parent::a

# button Add new 
# //a[@class='collapsed btn waves-effect waves-light btn-primary btn-sm m-0']
# //a[@class='btn btn-sm waves-effect waves-light btn-primary btn-icon m-0']/following-sibling::a

# textbox First Name
# //input[@name="first_name"]
# //label[@for="company_name"]/following-sibling::div/input

# textbox Last Name
# //input[@name="last_name"]
# //label[@for="last_name"]/following-sibling::div/input

# textbox Password
# //input[@name="password"]
# //label[@for="website"]/following-sibling::div/input


# textbox Contact Number
# //input[@name="contact_number"]
# //label[@for="contact_number"]/following-sibling::input

# textbox Gender
# //span[@class="select2-selection__rendered"]
# //span[@class='select2-selection__arrow']/preceding-sibling::span

# textbox Email
# //input[@name='email']
# //label[contains(text(),'Email')]/following-sibling::div/input


# textbox Username
# //input[@name='username']
# //label[contains(text(),'Username')]/following-sibling::div/input


# button Reset
# //button[@type='reset']
# //button[normalize-space()='Save']/preceding-sibling::button


# button Save
# //button[normalize-space()='Save']
# //button[@type='reset']/following-sibling::button