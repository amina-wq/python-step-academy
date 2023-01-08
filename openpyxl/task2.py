from openpyxl import Workbook
import task1

wb = Workbook()

sheet = wb.active 

arr = task1.arr

trans_arr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

for j, row in enumerate(arr, start=1):
    for i, value in enumerate(row, start=1):
        sheet.cell(row=i, column= j, value=value)

wb.save(filename= 'sheet2.xlsx')