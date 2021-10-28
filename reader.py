import xlrd, xlwt

rb = xlrd.open_workbook('C:\it\way\list_curr.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(380)]
new_vals = [x for xs in vals for x in xs]
print(new_vals)

# что то с ридингом xl файла 