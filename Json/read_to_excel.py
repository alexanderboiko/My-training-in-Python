# Как считывать данные из excel файла

import openpyxl

book = openpyxl.open('my_book.xlsx', read_only=True)
sheet = book.worksheets[0]
print(sheet['A3'])
# sheet = book.active

# cells = sheet['B1':'C11']
# for TITLE, YEAR in cells:
#     print(TITLE.value, YEAR.value)
# # print(sheet[1][2].value)
#
# for row in range(1,sheet.max_row+1):
#     ID = sheet[row][0].value
#     TITLE = sheet[row][1].value
#     YEAR = sheet[row][2].value
#     DIRECTOR = sheet[row][4].value
#     print(ID, TITLE, YEAR, DIRECTOR)

# for row in sheet.iter_rows(min_row= 2, max_row=20+1, min_col=1,max_col=3):
#     for cell in row:
#         print(cell.value, end=' ')
#     print()