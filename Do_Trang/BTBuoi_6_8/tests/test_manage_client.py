'''
Kịch bản 1:
1. Đăng nhập hệ thống
2. Truy cập chức năng ""Manage Client"" từ Menu
3. Click [Add New]
4. Nhập các trường thông tin bắt buộc
5. Click [Save]
6. Kiểm tra các dữ liệu vừa tạo trong Bảng ""List All Clients""
'''
from models.client import Client

def test_add_new_client(logged_in_manage_client):
    client = Client.create_data_manage_lient("input_data/client.json")

    logged_in_manage_client.go_to_manage_clients_page()
    logged_in_manage_client.create_client(client)
    logged_in_manage_client.verify_create_manage_client_success(client)