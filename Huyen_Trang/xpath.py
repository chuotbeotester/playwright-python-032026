Manage Clients:
#//span[normalize-space()='Manage Clients']
#//a[@href="https://hrm.anhtester.com/erp/clients-list"]

Button [+ Add New]
#//a[normalize-space()='Add New']
#//a[@href="https://hrm.anhtester.com/erp/clients-grid"]/following-sibling::a

First Name 
#//input[@name="first_name"]
#//label[contains(normalize-space(), "First Name")]/following-sibling::div//input

Last Name
#//input[@name="last_name"]
#//label[contains(normalize-space(), "Last Name")]/following-sibling::div//input

Password
#//input[@name="password"]
#//label[contains(normalize-space(), "Password")]/following-sibling::div//input

Contact Number
#//input[@name="contact_number"]
#//label[contains(normalize-space(), "Contact Number")]/following-sibling::input

Email
#//input[@name="email"]
#//label[contains(normalize-space(), "Email")]/following-sibling::div//input

Username
#//input[@name="username"]
#//label[contains(normalize-space(), "Username")]/following-sibling::div//input

Gender
#//span[@id="select2-gender-vg-container"]
#//select[@name="gender"]/following-sibling::span

Reset button
#//button[@type="reset"]
#//span[normalize-space()="Save"]/parent::button/preceding-sibling::button

Save button
#//span[normalize-space()="Save"]
#//button[@type="reset"]//following-sibling::button

Attachment
#//input[@type="file"]
#//label[@class="custom-file-label"]/preceding-sibling::input