from playwright.sync_api import expect
from .base_page import BasePage
from component.table import Table


class UserManagement(BasePage, Table):
    URL = "https://book.anhtester.com/user-management"

    def __init__(self, page):
        BasePage.__init__(self, page)
        Table.__init__(self, page)

    def navigate_to_page(self):
        self._goto(self.URL)
        
    def check_table_visible(self):
        self.table_visible()

    def get_cell_value(self, row, col):
         return self.get_table_cell( row, col)
    
    def get_rows_count(self):
        return self.get_row_count()

    def get_columns_count(self):
        return self.get_column_count()

    def get_value_column(self, col):
        return self.get_table_column(col)

    def get_value_row(self, row):
        return self.get_table_row(row)
    
    def get_data_table(self):
        return self.get_table()
    
    def find_row_by_key(self, key):
        return self.find_row(key)