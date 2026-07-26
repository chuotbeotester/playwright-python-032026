import pytest
from playwright.sync_api import Page
# from page.login_page import LoginPage
# from page.home_page import HomePage
from utils.text_data import TextData
from utils.path_helper import PathFile
from page.lead_page import LeadsPage

# # Khởi tạo đối tượng LoginPage với đối tượng Page
# login_page = LoginPage(Page)

# #Đăng nhập Login
# login_page.login(getcredential["URL"], getcredential["USERNAME"], getcredential["PASSWORD"])

# #Khởi tạo HomePage với đối tượng Page
# home_page = HomePage(Page)

# #Truy cập dashboard => Leads
# home_page.choose_left_menu("CRM", "Leads")

def test_add_new_lead(logged_in_leads):
    """
    Thêm một lead mới bằng cách sử dụng dữ liệu từ tệp JSON.

    Args:
        logged_in_leads (LeadsPage): Đối tượng LeadsPage đã đăng nhập.
    """
    #Khởi tạo LeadsPage với đối tượng Page
    lead_page = logged_in_leads
    
    #Đọc dữ liệu từ tệp JSON
    data = PathFile.read_json_data("input_data/leads.json")
    path_file = PathFile.get_string_file_path(data["pathFile"])
    
    #Sinh ngẫu nhiên để tạo tên lead duy nhất
    first_name = TextData.create_text_data(data["firstName"])
    last_name = data["lastName"]
    contact_number = data["contactNumber"]
    email = TextData.create_text_data("auto") + "@test.com"
    
    #Truy cập chức năng Leads
    #lead_page.go_to_lead_page(get_credential["URL"])
    
    #Nhập form "Add New Lead"
    lead_page.add_new_lead(first_name, last_name, contact_number, email, path_file)
    
    #Kiểm tra Lead vừa tạo trong "List All Leads"
    lead_page.verify_added_lead(first_name, last_name, email)
    

