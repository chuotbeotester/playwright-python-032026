# Thực hiện các action sau:
# 1. Click menu Manage Clients
# 2. Click button [+ Add New]
# 3. Nhập các trường thông tin sau:
#     + Textbox: First Name *, Last Name *, Password *, Contact Number *, Email *, Username *
#     + Lựa chọn dropdown list: Gender
#     + Upload file vào trường Attachment *
# 4. Click button [Save]
# 5. Nhập dữ liệu vào Textbox Search --> giá trị Email đã tạo ở Bước 3
# 6. Kiểm tra các cột thông tin ở bảng kết quả ở dưới những trường thông tin sau:
#     + Cột "Name": dòng đầu tiên hiển thị First Name đã nhập + Last Name đã nhập - dòng thứ 2 hiển thị Email đã nhập
#     + Cột "Username": hiển thị Username đã nhập
#     + Cột "Contact Number": hiển thị Contact Number đã nhập
#     + Cột "Gender": hiển thị Gender đã nhập
#     + Cột "Status": hiển thị "Active"

from playwright.sync_api import Page, expect

#Application URL
base_url = "https://hrm.anhtester.com/"
expected_url = "https://hrm.anhtester.com/erp/desk"
#Login credentials
login_username = "admin_example"
login_password = "123456"

#Login page locators

#Username input field
username_ipt = "Your Username"
#Password input field
password_ipt = "Enter Password"
#Login button
login_button = '//button[contains(@class,"btn-primary")]'

#Add new client locators

#Manage clients menu
manage_clients_menu = "Manage Clients"
#Add new button
add_new_button = "Add New"
#First name input field
first_name_ipt = "First Name"
#Last name input field
last_name_ipt = "Last Name"
#Client password input field
client_password_ipt = "Password"
#Contact number input field
contact_number_ipt = "Contact Number"
#Email input field
email_ipt = "Email"
#Username input field
client_username_ipt = "Username"
#Gender dropdown
gender_dropdown = "[data-placeholder='Gender']"
#File upload button
upload_button = "Choose File"
#Save button
save_button = "Save"
#Search box
search_box = "Search"

#Client information
first_name = "Nguyen"
last_name = "Hung"
client_password = "Test@12345"
contact_number = "0901234567"
email = "nguyenhung111@gmail.com"
client_username = "Iris Nguyen"
gender = "Male"
#Search keyword
search_keyword = "Nguyen Hung"
#Upload file path
profile_image = "Anh_Khoa/BTBuoi05/tests/ok.jpg"
#Expected status
expected_status = "Active"

#Table data locators of Manage Clients page

#Name column in search results
name_column = '//table[@id="xin_table"]//tbody//tr[1]//td[1]//h6'
#Email column in search results
email_column = '//table[@id="xin_table"]//tbody//tr[1]//td[1]//p'
#Usernam column in search results
username_column = '//table[@id="xin_table"]//tbody//tr[1]//td[2]'
#Contact Number column in search results
contact_number_column = '//table[@id="xin_table"]//tbody//tr[1]//td[3]'
#Gender column in search results
gender_column = '//table[@id="xin_table"]//tbody//tr[1]//td[4]'
#Status column in search results
status_column = '//table[@id="xin_table"]//tbody//tr[1]//td[6]//span'

#Delete client button
delete_button = "//button[contains(@class,'delete')]"
#Delete client popup confirm
delete_popup_confirm = "Are you sure you want to delete this record?"
#Confirm button
confirm_button = "//span[text()='Confirm']/parent::button"
#Notify deleted success
notify_deleted = "//div[text()='Client deleted.']"


def test_search(page: Page):

    #Navigate to HRM website
    page.goto(base_url)
    
    #Enter login username
    page.get_by_role("textbox", name=username_ipt).fill(login_username)
    #Enter login password
    page.get_by_role("textbox", name=password_ipt).fill(login_password)
    #Click login button
    page.locator(login_button).click()

    #Verify successful login
    expect(page).to_have_url(expected_url)

    #Open Manage Clients menu
    page.get_by_role("link", name=manage_clients_menu).click()

    #Verify menu is visible
    expect(page.get_by_role("link", name=manage_clients_menu)).to_be_visible()

    #Click Add New Client
    page.get_by_role("link", name=add_new_button).click()

    #Enter First Name
    page.get_by_role("textbox", name=first_name_ipt).fill(first_name)

    #Enter Last Name
    page.get_by_role("textbox", name=last_name_ipt).fill(last_name)

    #Enter Client Password
    page.get_by_role("textbox", name=client_password_ipt).fill(client_password)

    #Enter Contact Number
    page.get_by_placeholder(contact_number_ipt).fill(contact_number)

    #Enter Email
    page.get_by_role("textbox", name=email_ipt).fill(email)

    #Enter Username
    page.get_by_role("textbox", name=client_username_ipt).fill(client_username)

    #Select Male from Gender dropdown
    page.locator(gender_dropdown).select_option(label=gender)

    #Upload profile image
    page.get_by_role("button", name=upload_button).set_input_files(profile_image)

    #Save client information
    page.get_by_role("button", name=save_button).click()

    #Search for the newly created client
    page.get_by_role("searchbox", name=search_box).fill(search_keyword)

    #Verify Name
    expect(page.locator(name_column)).to_have_text(f"{first_name} {last_name}")

    #Verify Email
    expect(page.locator(email_column)).to_have_text(email)

    #Verify Username
    expect(page.locator(username_column)).to_have_text(client_username)

    #Verify Contact Number
    expect(page.locator(contact_number_column)).to_have_text(contact_number)

    #Verify Gender
    expect(page.locator(gender_column)).to_have_text(gender)

    #Verify Status
    expect(page.locator(status_column)).to_have_text(expected_status)

    #Delete client just created
    page.locator(delete_button).click()

    #Verify delete popup confirm visible
    expect(page.get_by_role("heading", name=(delete_popup_confirm))).to_be_visible()

    #Confirm delete client 
    page.locator(confirm_button).click()

    #Verify deleted success
    expect(page.locator(notify_deleted)).to_be_visible()