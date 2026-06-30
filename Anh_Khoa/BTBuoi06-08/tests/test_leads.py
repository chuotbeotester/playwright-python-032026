from page import LeadsPage


def test_create_lead(leads_page: LeadsPage, leads_data: dict):
    leads_page.go_to_leads_page()
    leads_page.create_lead(
        first_name=leads_data["first_name"],
        last_name=leads_data["last_name"],
        gender=leads_data["gender"],
        contact_number=leads_data["contact_number"],
        email=leads_data["email"],
        file_path=leads_data["file_path"],
    )
    leads_page.verify_lead_created(leads_data["first_name"], leads_data["last_name"])
