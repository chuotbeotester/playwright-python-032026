from API.Auth_API import Auth
from pages.UI.Book.login_page import LoginBook
from pages.UI.Book.user_management import UserManagement
from playwright.sync_api import Page 
import time

def test_verify_API_created_success(page, api_context, new_user_data):
    auth = Auth(api_context)
    response = auth.register(new_user_data)
    assert response.status == 201

    login = LoginBook(page)
    login.goto("https://book.anhtester.com/sign-in")

    login.login("auto245@gmail.com", "Test123@")

    user = UserManagement(page)
    user.goto()
    user.search_username(new_user_data["email"])
    user.edit_user()
    time.sleep(6)

