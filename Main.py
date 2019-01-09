from CreateExcel import createExcel
from ParseExcel import *

#createExcel()

parsedExcel = ParseExcel('sample.xlsx')
sheet = parsedExcel.getSheet('Sheet')
#parseList = parsedExcel.getParsedExcelList(sheet)
parsedExcel.addToDatabase(sheet)
print(parsedExcel.selectAll())

