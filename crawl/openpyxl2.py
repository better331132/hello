import openpyxl
book = openpyxl.Workbook()
sheet1 = book.active
# tmpCell = sheet['C1']
for i in range(1,100):
    tmpCell = sheet1.cell(row=i, column=3)
    tmpCell.font = openpyxl.styles.Font(size=14, color='FF0000')
    tmpCell.value = i
    tmpCell.number_format
book.save("./data/openpyxl2.xlsx")