# Menu Manage Clients
//a[contains(@href,'clients-list')]
//span[@class='pc-mtext' and normalize-space()='Manage Clients']/parent::a

# Button Add new
//a[contains(@class,'btn-primary') and normalize-space(.)='Add New']
//a[@href='#add_form']/preceding-sibling::a[contains(@href,'clients-grid')]

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
//span[@class='ladda-spinner']/preceding-sibling::span[normalize-space()='Save']/parent::button
//button[@type='reset']/following-sibling::button[@type='submit']

# Attechment
//input[@type='file' and @name='file']
//div[@class='custom-file']/child::input[@type='file']