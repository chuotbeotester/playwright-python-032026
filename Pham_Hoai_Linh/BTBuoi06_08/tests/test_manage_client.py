import pytest
from utils.path_helper import PathFile



def test_add_new_client(logged_in_manageClient, get_client_infor, get_avatar_path):
    logged_in_manageClient.go_to_manage_client_page()
    logged_in_manageClient.add_new_client(
        get_client_infor["firsname"],
        get_client_infor["lastname"],
        get_client_infor["password"],
        get_client_infor["contactNumer"],
        get_client_infor["gender"],
        get_client_infor["email"],
        get_client_infor["userName"],
        str(get_avatar_path)
    )
    logged_in_manageClient.verify_added_client(
        get_client_infor["firsname"],
        get_client_infor["lastname"],
        get_client_infor["contactNumer"],
        get_client_infor["gender"],
        get_client_infor["email"],
        get_client_infor["userName"]
        )