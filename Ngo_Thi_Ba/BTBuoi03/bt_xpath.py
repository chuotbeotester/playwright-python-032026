# "Truy cập trang: https://hrm.anhtester.com/
# Username: admin_example
# Password: 123456"

Bài tập 1: Xác định XPath các element sau: 
    1: Menu Manage Client
    C1: //a [@href="https://hrm.anhtester.com/erp/clients-list" ]  
    C2: //span[normalize-space()='Manage Clients']
    
    2. Button [+Add New]
    C1: //a[normalize-space()= "+ Add New"]
    C2: //div[@class ="card user-profile-list"]/div/div/a[2]
    
    3. Các trường thông tin: 
        3.1: Textbox
            - First Name *:
                + //input[@name='first_name']
                + //label[contains(text(),'First Name')]/following::input[1]
            - Last name *: 
                + //input[@name='last_name']
                + //label[contains(text(),'Last Name')]/following::input[1]
            - Passwword *: 
                + //input[@name='password']
                + //label[contains(text(),'Password')]/following::input[1]
            - Contact Number *: 
                + //input[@name='contact_number']
                + //label[contains(text(),'Contact Number')]/following::input[1]
            - Email *: 
                + //input[@name='email']
                + //label[contains(text(),'Email')]/following::input[1]
            - Username *: 
                + //input[@name='username']
                + //label[contains(text(),'Username')]/following-sibling::div//input
        3.2: Gender: 
                + //select[@name='gender']
                + //div[contains(@class,'form-group')]//select[@name='gender']
        3.3: Button [Reset]: 
                + //button[@type='reset']
                + //*[normalize-space()='Reset']
             Button [Save]: 
                + //button[@type='submit']
                + //*[normalize-space()='Save']
        3.4: Thẻ <input> trong trường Attachment *: 
            + //input[@type='file']
            + //label[contains(text(),'Attachment')]/following::input[1]