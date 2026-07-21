from page import ManageClientPage


def test_create_manage_client(manage_client_page: ManageClientPage, manage_client_data: dict):
    manage_client_page.go_to_manage_clients_page()
    manage_client_page.create_client(
        first_name=manage_client_data["first_name"],
        last_name=manage_client_data["last_name"],
        password=manage_client_data["password"],
        contact_number=manage_client_data["contact_number"],
        gender=manage_client_data["gender"],
        email=manage_client_data["email"],
        username=manage_client_data["username"],
        file_path=manage_client_data["file_path"],
    )
    manage_client_page.verify_client_created(manage_client_data["first_name"], manage_client_data["last_name"])
