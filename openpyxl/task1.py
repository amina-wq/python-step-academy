from openpyxl import Workbook, load_workbook

wb = load_workbook(filename= 'sheet.xlsx')
sheet = wb['Sheet1']
arr = []

for row in sheet:
    arr.append([cell.value for cell in row])

for row in arr:
    for cell_value in row:
        print(cell_value, end= ' ')
    print()