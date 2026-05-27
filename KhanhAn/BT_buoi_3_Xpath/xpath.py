# URL bai tap: 
# Dashboard: https://hrm.anhtester.com/erp/desk?module=dashboard
# Client list: https://hrm.anhtester.com/erp/clients-list

# Step1: Menu Manage Clients
# Menu Manage Clients: 
# //a[@href="https://hrm.anhtester.com/erp/clients-list"]
# //span[normalize-space()="Manage Clients"]/ancestor::a

# Step2: Button [+ Add New]
# Add New button: 
# //a[@class="collapsed btn waves-effect waves-light btn-primary btn-sm m-0"]
# //div[@id="xin_table_wrapper"]/ancestor::div//a[normalize-space()="Add New"]

# Step3: Click vao Button [+ Add New] va xac dinh cac truong hop:
#Text box First Name: 
# //input[@name="first_name"]
# //label[@for="company_name"]/following-sibling::div/input

#Text box Last Name: 
# //input[@name="last_name"]
# //label[@for="last_name"]/following-sibling::div/input

#Text box Password: 
# //input[@name="password"]
# //label[@for="website"]/following-sibling::div/input

#Text box Contact Number: 
# //input[@name="contact_number"]
# //label[@for="contact_number"]/following-sibling::input

#Text box Email: 
# //input[@name="email"]
# //label[contains(text(),"Email")]/following-sibling::div/input

#Text box Username: 
# //input[@name="username"]
# //label[contains(text(),'Username')]/following-sibling::div/input

#Drop down list Gender: 
# //span[@class="selection"]
# //select[@name="gender"]/following-sibling::span

#Button Reset: 
# //button[normalize-space()="Reset"]
# //*[normalize-space()="Add New Client"]/ancestor::div//button[contains(text(),"Reset")]

#Button Save: 
# //span[normalize-space()="Save"]
# //*[normalize-space()="Add New Client"]/ancestor::div//button/span[contains(text(),"Save")]

#Input in Attachment: 
# //input[@name="file"]
# //label[@class="custom-file-label"]/preceding-sibling::input