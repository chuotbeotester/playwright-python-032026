import pytest
import random
from playwright.sync_api import Page
from utils.path_helper import PathFile
from page.manage_clients_page import ManageClientsPage


def test_add_new_client(logged_in_manage_clients):
    """
    Thêm một client mới bằng cách sử dụng dữ liệu từ tệp JSON.

    Args:
        logged_in_manage_clients (ManageClientsPage): Đối tượng ManageClientsPage đã đăng nhập.
        manage_client (dict): Dữ liệu client từ tệp JSON.
    """
    # Khởi tạo ManageClientsPage với đối tượng Page
    manage_clients_page = logged_in_manage_clients

    #Đọc dữ liệu từ tệp JSON
    data = PathFile.read_json_data("input_data/manage_client.json")
    path_file = data["pathFile"]

    # Sinh ngẫu nhiên để tạo tên client duy nhất
    first_name = data["firstName"] + str(random.randint(1000, 9999))
    last_name = data["lastName"]
    contact_number = data["contactNumber"]
    email = f"auto_{random.randint(1000,9999)}@test.com"
    password = data["password"]
    username = data["userName"] + str(random.randint(1000, 9999))
    attachment = data["pathFile"]

    # Truy cập chức năng Manage Clients
    manage_clients_page.go_to_manage_clients_page()

    # Nhập form "Add New Client"
    manage_clients_page.add_new_client(first_name, last_name, password, email, contact_number, username, attachment)

    # Kiểm tra Client vừa tạo trong "List All Clients"
    manage_clients_page.verify_added_client(email)