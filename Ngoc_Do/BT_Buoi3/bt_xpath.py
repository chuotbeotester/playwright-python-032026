#https://hrm.anhtester.com/erp/desk?module=dashboard
#Manage Client
//a[normalize-space() ="Manage Clients"]
//span[normalize-space() ="Manage Clients"]/ancestor::a


#https://hrm.anhtester.com/erp/clients-list
#Add New Button
//a[normalize-space() ="Add New"]
//div[@id ="xin_table_wrapper"]/ancestor::div//a[normalize-space() ="Add New"]


#First Name
//input[@name="first_name"]
//label[@for="company_name"]/following-sibling::div/input


#Last Name
//input[@name="last_name"]
//label[@for="last_name"]/following-sibling::div/input


#Password
//input[@name="password"]
//label[@for="website"]/following-sibling::div/input


#Contact Number
//input[@name="contact_number"]
//label[@for='contact_number']/following-sibling::input


#Gender
//span[@class="selection"]
//select[@name="gender"]/following-sibling::span


#Email
//input[@name ="email"]
//label[@for="email"]/following-sibling::div/input[@name="email"]


#Username
//input[@name="username"]
//label[@for="email"]/following-sibling::div/input[@name="username"]


#Reset Button
//button[normalize-space()="Reset"]
//div[@id="xin_table_wrapper"]/ancestor::div//button[normalize-space()="Reset"]


#Save Button
//button[normalize-space()="Save"]
//div[@id="xin_table_wrapper"]/ancestor::div//button[normalize-space()="Save"]


#Attachment
//input[@class="custom-file-input"]
//label[@for="logo"]/following-sibling::div/input
