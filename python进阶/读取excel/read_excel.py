import xlrd

book = xlrd.open_workbook("./income.xlsx")

print(f"包含表单数量:{book.nsheets}")
print(f"表单的名称分别为:{book.sheet_names()}")

sheet = book.sheet_by_index(0)
print(f"表单名：{sheet.name} ")
print(f"表单索引：{sheet.number}")
print(f"表单行数：{sheet.nrows}")
print(f"表单列数：{sheet.ncols}")
print(f"单元格A1内容是:{sheet.cell_value(rowx=0,colx=0)}")
print(f"第一行内容是: {sheet.row_values(rowx=0)}")
print(f"第一列内容是:{sheet.col_values(colx=0)}")
book.sheet_by_name("2018")
book.sheets()


