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
import time

name_column = '//table[@id="xin_table"]//tbody//tr[1]//td[1]//h6'
email_column = '//table[@id="xin_table"]//tbody//tr[1]//td[1]//p'
username_column = '//table[@id="xin_table"]//tbody//tr[1]//td[2]'
contact_number_column = '//table[@id="xin_table"]//tbody//tr[1]//td[3]'
gender_column = '//table[@id="xin_table"]//tbody//tr[1]//td[4]'
status_column = '//table[@id="xin_table"]//tbody//tr[1]//td[6]//span'

def test_search(page: Page):

    page.goto("https://hrm.anhtester.com/")
    
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.locator('//button[contains(@class,"btn-primary")]').click()

    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk")

    page.get_by_role("link", name="Manage Clients").click()

    expect(page.get_by_role("link", name="Manage Clients")).to_be_visible()

    page.get_by_role("link", name="Add New").click()

    page.get_by_role("textbox", name="First Name").fill("Nguyen")

    page.get_by_role("textbox", name="Last Name").fill("Hung")

    page.get_by_role("textbox", name="Password").fill("Test@12345")

    page.get_by_placeholder("Contact Number").fill("0901234567")

    page.get_by_role("textbox", name="Email").fill("nguyenhung111@gmail.com")

    page.get_by_role("textbox", name="Username").fill("Iris Nguyen")

    page.locator("[data-placeholder='Gender']").select_option(label="Male")

    page.get_by_role("button", name="Choose File").set_input_files("BTBuoi05/tests/ok.jpg")

    page.get_by_role("button", name="Save").click()

    page.get_by_role("searchbox", name="Search").fill("Nguyen Hung")

    expect(page.locator(name_column)).to_have_text("Nguyen Hung")

    expect(page.locator(email_column)).to_have_text("nguyenhung111@gmail.com")

    expect(page.locator(username_column)).to_have_text("Iris Nguyen")

    expect(page.locator(contact_number_column)).to_have_text("0901234567")

    expect(page.locator(gender_column)).to_have_text("Male")

    expect(page.locator(status_column)).to_have_text("Active")