from pages.user_management import UserManagement
import time
def test_read_cell_table(page):
    user_page = UserManagement(page)
    user_page.navigate_to_page()
    # user_page.check_table_visible()
    user_page.check_table_visible()
    # time.sleep(2)
    # print(user_page.get_rows_count())
    # print(user_page.get_columns_count())
    # print(user_page.get_cell_value(3,0))
    # print(user_page.get_value_column(4))
    # print(user_page.get_value_row(1))
    # print(user_page.get_data_table())
    n = user_page.find_row_by_key("bintestsecurity568@gmail.com")
    print("So dong chua key la: ", n)