import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

workbook = excel.Workbooks.Open(r"E:\231软件测试实战\python进阶\读取excel\income.xlsx")

sheet = workbook.Sheets('2017')

sheet.Cells(1, 1).Value = "你好"

workbook.Save()

workbook.Close()

excel.Quit()

sheet = None

book = None
excel.Quit()
excel = None
