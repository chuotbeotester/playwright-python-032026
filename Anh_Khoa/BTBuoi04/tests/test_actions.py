# Truy cập trang: https://hrm.anhtester.com/
# Username: admin_example
# Password: 123456
# Thực hiện các action sau:
# 1. Click menu Manage Clients
# 2. Click button [+ Add New]
# 3. Nhập các trường thông tin sau:
#     + Textbox: First Name *, Last Name *, Password *, Contact Number *, Email *, Username *
#     + Lựa chọn dropdown list: Gender
#     + Upload file vào trường Attachment *
# 4. Click button [Save]
from playwright.sync_api import Page
import time

def test_action(page: Page):

    page.goto("https://hrm.anhtester.com/")
    
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[contains(@class,"btn-primary")]').click()

    page.get_by_role("link", name="Manage Clients").click()

    page.get_by_role("link", name="Add New").click()

    page.get_by_role("textbox", name="First Name").fill("Nguyen")

    page.get_by_role("textbox", name="Last Name").fill("Khoa")

    page.get_by_role("textbox", name="Password").fill("Anhkhoa136!@")

    page.get_by_placeholder("Contact Number").fill("0905499300")

    page.get_by_role("textbox", name="Email").fill("ankhoa130600@gmail.com")

    page.get_by_role("textbox", name="Username").fill("Ethen Nguyen")

    page.locator("[data-placeholder='Gender']").select_option(label="Male")

    page.get_by_role("button", name="Choose File").set_input_files("BTBuoi04/tests/neko.jpg")

    page.get_by_role("button", name="Save").click()

    time.sleep(5)
    