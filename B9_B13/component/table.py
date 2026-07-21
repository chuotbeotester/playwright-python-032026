from playwright.sync_api import Page, expect

class Table():
    def __init__(self, page: Page):
        self.page = page
        self.table = self.page.locator("table")
        self.header = self.page.locator("thead th")
        self.row = self.table.locator("tbody tr")
    
    def table_visible(self):
        expect(self.row).to_be_visible()

    def get_row_count(self):
        return self.row.count()
    
    def get_column_count(self):
        return self.header.count()
    
    def get_table_cell(self, row_index, col_index):
        return (
            self.row
            .nth(row_index)
            .locator("td")
            .nth(col_index)
            .inner_text()
            .strip()
        )
    
    def get_table_column(self, col):
        data = []
        for i in range(self.get_row_count()):
            data.append(self.get_table_cell(i, col))
        return data
        # return [
        #     self.get_table_cell(i, col)
        #     for i in range(self.get_row_count())
        # ]
    
    def get_table_row(self, row):
        cells = self.row.nth(row).locator("td")
        data_row = []
        for i in range (cells.count()):
            data_row.append(cells.nth(i).inner_text().strip())
        return data_row

    def get_table(self):
        data_table = []
        for i in range(self.get_row_count()):
            data_table.append(self.get_table_row(i))
            # print(self.get_table_row(i))
        return data_table

    def find_row(self, key):
        rows = []
        for i in range(self.get_row_count()):
            r = self.row.nth(i)
            if key in r.inner_text():
                rows.append(i+1)
        return rows