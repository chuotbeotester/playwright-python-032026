# Menu Manage Clients
//a[normalize-space(text())='Manage Clients']
//span[@class='pc-mtext' and normalize-space()='Manage Clients']/parent::a

# Button Add new
//a[contains(@class,'btn-primary') and contains(text(),'Add New')]
//div[@class='card-header-right']/descendant::a[contains(text(),'Add New')]

# First Name
//input[@placeholder='First Name']
//form[@id='xin-form']/descendant::input[@name='first_name']

# Last Name
//input[@placeholder='Last Name']
//form[@id='xin-form']/descendant::input[@name='last_name']

# Password
//input[@placeholder='Password']
//form[@id='xin-form']/descendant::input[@name='password']

# Contact Number
//input[@placeholder='Contact Number']
//label[@for='contact_number']/following-sibling::input

# Gender
//select[@name='gender']
//select[@name='gender']/parent::div/descendant::span[@role='combobox']

# Email
//input[@placeholder='Email']
//form[@id='xin-form']/descendant::input[@name='email']

# Username
//input[@placeholder='Username']
//form[@id='xin-form']/descendant::input[@name='username']

# Reset
//button[@type='reset']
//div[@class='card-footer text-right']/descendant::button[@type='reset']

# Save
//button[@type='submit']
//button[@type='reset']/following-sibling::button[@type='submit']

# Attechment
//input[@type='file']
//input[@type='file']/following-sibling::label[@class='custom-file-label']