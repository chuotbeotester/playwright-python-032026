'''
Thực hiện các action sau:
1. Click menu Manage Clients
2. Click button [+ Add New]
3. Nhập các trường thông tin sau:
    + Textbox: First Name *, Last Name *, Password *, Contact Number *, Email *, Username *
    + Lựa chọn dropdown list: Gender
    + Upload file vào trường Attachment *
4. Click button [Save]
'''

from playwright.sync_api import Page
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