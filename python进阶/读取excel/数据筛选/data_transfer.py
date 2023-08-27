import json
import openpyxl
from datetime import datetime


# 文档结构
# all
#  -several days
#    -several ships
def extract(ship, time_obj):
    ship_info = {
        '计划时间': time_obj.strftime("%Y%m%d"),
        '中文船名': ship.get('shipNameCn'),
        '船长': ship.get('shipLength'),
        '吃水': ship.get('draft'),
        '动态': ship.get('dynamicName'),
        '起点泊位': ship.get('startBerth'),
        '终点泊位': ship.get('endBerth'),
        '主引': ship.get('master'),
        '副引': ship.get('assistant'),
        '其它引水': None,
        '代理': ship.get('orgShort'),
        '代理电话': ship.get('dTelephone'),
        '交通船': None,
        '航道': ship.get('channelName'),
        '侧推': f"首:{ship.get('headThrusterStatus')} 尾:{ship.get('tailThrusterStatus')}",
        '备注': ship.get('remarks')

    }
    return ship_info


with open('./info1.txt', 'r') as f:
    content = f.readlines()

target_info = []

for line in content:
    day = json.loads(line)
    for ship in day:
        time_str = ship.get('startWorkTime')
        if time_str:
            time_obj = datetime.strptime(time_str[:10], "%Y-%m-%d")
        else:
            continue
        if time_obj.strftime("%Y%m%d") == '20190108':
            target_info.append(extract(ship, time_obj))


book = openpyxl.Workbook()
sheet = book.active
sheet.title = '引航表'
header_row = sheet.append(list(target_info[0].keys()))

for info in target_info:
    row = [info[key] for key in info]
    sheet.append(row)

book.save('引航表-new.xlsx')
