from openpyxl import load_workbook
from dbconnect.dbconnect import *


class AddRatesToDB:

    def __init__(self, excel_file, sheet_name):

        try:
            self.wb = load_workbook(excel_file)
            sheet = self.wb[sheet_name]
            for row in sheet.rows:
                insert_rates(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    AddRatesToDB('rates.xlsx', 'Sheet')
