import xlrd
filename = "xls1.xls"
workbook = xlrd.open_workbook(filename)
sheet = workbook.sheets()[0]
rownum = sheet.nrows
colnum = sheet.ncols
for i in range(rownum):
    rowData = sheet.row_values(i)
    for item in rowData:
        print(item,end = ' ')
    print('')