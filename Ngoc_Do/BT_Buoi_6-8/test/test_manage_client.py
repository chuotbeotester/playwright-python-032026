import pytest
from utils.client import Client


NEW_CLIENT = Client.create_text_data()


def test_add_new_client(logged_in_manage_clients):
    logged_in_manage_clients.go_to_manage_clients_page()
    logged_in_manage_clients.create_client(NEW_CLIENT)
    logged_in_manage_clients.verify_create_success(NEW_CLIENT)
