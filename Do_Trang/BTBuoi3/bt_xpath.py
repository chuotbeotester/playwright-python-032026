# BT1: Menu Manage Clients
# //*[@class="feather feather-user-check"]/ancestor::a[@class="pc-link "]
# //a[@href="https://hrm.anhtester.com/erp/clients-list"]
# //span[normalize-space()="Manage Clients"]/parent::a

# BT2: btn Add New
# //a[normalize-space()="Add New"]
# //*[@class="feather feather-plus"]/parent::a

# BT3:
# # textbox First name:
# //input[@name="first_name"]
# //label[contains(text(),'First Name')]/following-sibling::div/input

# # textbox Last name:
# //input[@name="last_name"]
# //label[contains(text(),'Last Name')]/following-sibling::div/input

# # textbox Password:
# //input[@name="password"]
# //label[contains(text(),'Password')]/following-sibling::div/input

# # textbox Contact Number:
# //input[@name="contact_number"]
# //label[@for="contact_number"]/following-sibling::input

# # textbox Email:
# //input[@name="email"]
# //label[contains(text(),'Email')]/following-sibling::div/input

# # textbox User name:
# //input[@name="username"]
# //label[contains(text(),'Username')]/following-sibling::div/input

# # Dropdown list Gender:
# //select[@name="gender"]
# //label[contains(text(),'Gender')]/following-sibling::select

# # Btn Reset
# //button[@href="#add_form"]
# //span[normalize-space()="Save"]/preceding::button

# # Btn Save
# //span[normalize-space()="Save"]/parent::button
# //button[@href="#add_form"]/following-sibling::button

# # Thẻ input trong trường Attachment
# //input[@name="file"]
# //label[@class="custom-file-label"]/preceding-sibling::input
