import openpyxl

name2age = [
    ['张飞', 38],
    ['赵云', 27],
    ['许褚', 36],
    ['典韦', 38],
    ['关羽', 39],
    ['黄忠', 49],
    ['徐晃', 43],
    ['马超', 23]
]

book = openpyxl.Workbook()
sh = book.active
sh.title = '年龄表'

sh['A1'] = '姓名'
sh['B1'] = '年龄'

for row in name2age:
    sh.append(row)

book.save('信息表2.xlsx')
