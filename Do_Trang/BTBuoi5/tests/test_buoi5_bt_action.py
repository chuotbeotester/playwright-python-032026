'''
Thực hiện các action sau:
1. Click menu Manage Clients
2. Click button [+ Add New]
3. Nhập các trường thông tin sau:
    + Textbox: First Name *, Last Name *, Password *, Contact Number *, Email *, Username *
    + Lựa chọn dropdown list: Gender
    + Upload file vào trường Attachment *
4. Click button [Save]
5. Nhập dữ liệu vào Textbox Search --> giá trị Email đã tạo ở Bước 3
6. Kiểm tra các cột thông tin ở bảng kết quả ở dưới những trường thông tin sau:
    + Cột ""Name"": dòng đầu tiên hiển thị First Name đã nhập + Last Name đã nhập - dòng thứ 2 hiển thị Email đã nhập
    + Cột ""Username"": hiển thị Username đã nhập
    + Cột ""Contact Number"": hiển thị Contact Number đã nhập
    + Cột ""Gender"": hiển thị Gender đã nhập
    + Cột ""Status"": hiển thị ""Active""
'''

from playwright.sync_api import Page, expect
from datetime import datetime
from pathlib import Path


first_name = "Do"
last_name = "Thu Trang"
password = "123456"
contact_number = "0123456789"
current_time = datetime.now().strftime("%H%M%S")
email = f"trang{current_time}@gmail.com"
user_name = f"dotrang{current_time}"
gender = "Female"
path_file_img = Path(__file__).resolve().parent / "Download.png"
full_name = f"{first_name} {last_name}"

def test_buoi5_bt_action(page : Page):
    page.goto("https://hrm.anhtester.com/")

    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[contains(@class, "btn-primary")]').click()

    # 1. CLick menu Manage Clients
    page.get_by_role("link", name="Manage Clients").click()

    # 2. CLick btn Add New
    page.get_by_role("link", name="Add New").click()

    # 3. Nhập các trường thông tin
    # First Name
    page.get_by_role("textbox", name="First Name").fill(first_name)
    # Last Name
    page.get_by_role("textbox", name="Last Name").fill(last_name)
    # Password
    page.get_by_role("textbox", name="Password").fill(password)
    # Contact Number
    page.locator('//input[@name="contact_number"]').fill(contact_number)
    # Email
    page.get_by_role("textbox", name="Email").fill(email)
    # Username
    page.get_by_role("textbox", name="Username").fill(user_name)
    # Droplist Gender
    page.locator("//select[@name='gender']").select_option(label = gender)
    # Upload file vào trường Attachment
    page.get_by_role("button", name="Choose File").set_input_files(path_file_img)
    
    # 4. Click btn Save
    page.get_by_role("button", name="Save").click()

    # 5. Nhập dữ liệu vào Textbox Search --> giá trị Email đã tạo
    page.get_by_role("searchbox", name="Search").fill(email)

    # 6. Kiểm tra các cột thông tin ở bảng kết quả
    # Lấy dòng đầu tiên của bảng
    first_row = page.locator("//table[@id='xin_table']//tbody/tr")

    # Verify Name 
    expect(first_row.locator("xpath=.//h6")).to_have_text(full_name)
    expect(first_row.locator("xpath=.//p")).to_have_text(email)

    # Verify Username
    expect(first_row.locator("xpath=./td[2]")).to_have_text(user_name)

    # Verify Contact Number
    expect(first_row.locator("xpath=./td[3]")).to_have_text(contact_number)

    # Verify Gender 
    expect(first_row.locator("xpath=./td[4]")).to_have_text(gender)

    # Verify Status
    expect(first_row.locator("xpath=./td[6]")).to_have_text("Active")