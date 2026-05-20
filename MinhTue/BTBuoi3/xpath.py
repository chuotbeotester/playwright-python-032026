
# 1. Menu "Manage Clients"
menu_manage_clients_1 = "//a[normalize-space()='Manage Clients']"
menu_manage_clients_2 = "//span[normalize-space() ='Manage Clients']/ancestor::a" 

# 2. Button [+ Add New]
btn_add_new_1 = "//a[normalize-space()='Add New']"
btn_add_new_2 = "//*[name()='svg' and contains(@class,'feather feather-plus')]/parent::a" 


# 3. Textbox: First Name 
txt_first_name_1 = "//input[@name='first_name']"
txt_first_name_2 = "//label[@for='company_name']/following-sibling::div/input"
# 4. Textbox: Last Name 
txt_last_name_1 = "//input[@name='last_name']"
txt_last_name_2 = "//label[@for='last_name']/following-sibling::div/input"  


# 5. Textbox: Password 
txt_password_1 = "//input[@name='password']"
txt_password_2 = "//label[@for='website']/following-sibling::div/input"  


# 6. Textbox: Contact Number 

txt_contact_number_1 = "//input[@name='contact_number']"
txt_contact_number_2 = "//label[@for='contact_number']/following-sibling::input" 


# 7. Textbox: Email 

txt_email_1 = "//input[@name='email']"
txt_email_2 = "//label[contains(text(),'Email')]/following-sibling::div/input" 


# 8. Textbox: Username 

txt_username_1 = "//input[@name='username']"
txt_username_2 = "//label[contains(text(),'Username')]/following-sibling::div/input"  



# 9. Dropdown list: Gender

dropdown_gender_1 = "//select[@name='gender']"
dropdown_gender_2 = "//label[@for='gender']/following-sibling::select" 



# 10. Button [Reset]

btn_reset_1 = "//button[@type='reset']"
btn_reset_2 = "//button[@type='submit']/preceding-sibling::button[@type='reset']"  

# 11. Button [Save]

btn_save_1 = "//button[@type='submit']"
btn_save_2 = "//button[@type='reset']/following-sibling::button[@type='submit']" 

# 12. Thẻ <input> trong trường Attachment 

input_attachment_1 = "//input[@type='file']"
input_attachment_2 = "//label[@class='custom-file-label']/preceding-sibling::input"  