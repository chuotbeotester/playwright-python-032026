
# Menu Manage Clients (from Home page): //a[@href="https://hrm.anhtester.com/erp/clients-list"]
# Menu Manage Clients (from Home page): //span[normalize-space() = "Manage Clients"]//parent::a

# Add new button: //a[class="collapsed btn waves-effect waves-light btn-primary btn-sm m-0"]
# Add new button: //a[@class="btn btn-sm waves-effect waves-light btn-primary btn-icon m-0"]/following-sibling::a

# Textbox First Name: //input[@name="first_name"]
# Textbox First Name: //label[@for="company_name"]/following-sibling::div/input

# Textbox Last Name: //input[@name="last_name"]
# Textbox Last Name: //label[@for="last_name"]/following-sibling::div/input

# Textbox Password: //input[@name="password"]
# Textbox Password: //label[@for="website"]/following-sibling::div/input

# Textbox Contact Number: //input[@name="contact_number"]
# Textbox Contact Number: //label[@for="contact_number"]/following-sibling::input

# Textbox Email: //input[@name="email"]
# Textbox Email: //i[@class="fas fa-envelope"]/parent::span/following::input[1]

# Textbox Username: //input[@name="username"]
# Textbox Username: //label[contains(text(), "Username")]/following-sibling::div/input

# Dropdown list: Gender //select[@class="form-control select2-hidden-accessible"]
# Dropdown list: Gender //span[@dir="ltr"]/preceding-sibling::select

# Button [Reset]: //button[@type="reset"]
# Button [Reset]: //span[normalize-space()="Save"]/parent::button/preceding-sibling::button

# Thẻ <input>  trong trường Attachment: //input[@class="custom-file-input"]
# Thẻ <input>  trong trường Attachment //label[@class="custom-file-label"]/preceding-sibling::input