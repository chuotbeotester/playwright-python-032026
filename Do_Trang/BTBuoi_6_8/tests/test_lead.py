'''
Kịch bản 2:
1. Đăng nhập hệ thống
2. Truy cập chức năng ""Leads"" từ Menu
3. Click [Add New]
4. Nhập các trường thông tin bắt buộc
5. Click [Save]
6. Kiểm tra các dữ liệu vừa tạo trong Bảng ""List All Leads""
'''
from models.lead import Lead

def test_add_new_client(logged_in_leads):
    lead = Lead.create_data_lead("input_data/leads.json")

    logged_in_leads.go_to_lead_page()
    logged_in_leads.create_leads(lead)
    logged_in_leads.verify_create_leads_success(lead)
