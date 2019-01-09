from openpyxl import load_workbook
from pprint import *
from dbconnect.dbconnect import *


class ParseExcel:

    def __init__(self, fileName):
        self.fileName = fileName
        self.wb = load_workbook(self.fileName)

    def getSheet(self, sheet_name):
        sheet = self.wb[sheet_name]
        return sheet


    def getParsedExcelList(self, sheet):
        parsedList = list()
        for row in sheet.rows:
            cell_value = ''
            for cell in row:
                cell_value += (cell.value) + ' '
            parsedList.append(cell_value)
        return parsedList


    def addToDatabase(self, sheet):
        try:
            for row in sheet.rows:
                insert_contact(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
            return True

        except Exception as e:
            return e


    def selectAll(self):
        items = select_all()
        for i in items:
            print(i)


