#Menu Manage Clients: //a[normalize-space() ='Manage Clients']
#Menu Manage Clients: //span[normalize-space() ='Manage Clients']/ancestor::a

#Add New button: //a[normalize-space() ='Add New']
#Add New button: //div[@id ='xin_table_wrapper']/ancestor::div//a[normalize-space() ='Add New']

#Text box First Name: //input[@name ='first_name']
#Text box First Name: //label[@for='company_name']/following-sibling::div/input

#Text box Last Name: //input[@name ='last_name']
#Text box Last Name: //label[@for='last_name']/following-sibling::div/input

#Text box Password: //input[@name ='password']
#Text box Password: //label[@for='website']/following-sibling::div/input

#Text box Contact Number: //input[@name ='contact_number']
#Text box Contact Number: //label[@for='contact_number']/following-sibling::input

#Text box Email: //input[@name ='email']
#Text box Email: //label[contains(text(),'Email')]/following-sibling::div/input

#Text box Username: //input[@name ='username']
#Text box Username: //label[contains(text(),'Username')]/following-sibling::div/input

#Drop down lis Gender: //span[@class="selection"]
#Drop down lis Gender: //select[@name="gender"]/following-sibling::span

#Button Reset: //button[contains(text(), 'Reset')]
#Button Reset: //h5[normalize-space()='Add New Client']/ancestor::div//button[contains(text(), 'Reset')]

#Button Save: //button[contains(text(), 'Save')]
#Button Save: //h5[normalize-space()='Add New Client']/ancestor::div//button/span[contains(text(), 'Save')]

#Input in Attachment: //input[@name="file"]
#Input in Attachment: //label[@class="custom-file-label"]/preceding-sibling::input