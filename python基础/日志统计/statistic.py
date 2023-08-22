with open('2019-10-22_11.05.40.log', 'r', encoding='utf8') as f:
    content = f.readlines()

for index, line in enumerate(content):
    content[index] = line.split('|')

lineLen = {}

# 测试之后发现,若用'|'对字段进行分割, 根据分割的长度可以分为若干种不同的类型
for line in content:
    if len(line) not in lineLen:
        key = len(line)
        lineLen[key] = {'amount': 1, 'lines': [line]}
    else:
        lineLen[len(line)]['amount'] += 1
        lineLen[len(line)]['lines'].append(line)
# print(lineLen)  # 有两种,len =  3为未超时, len = 4未超时

# 传入保存了所有 len = x的列表的列表, index为响应时间在列表中的位置
def statistic(linelist,index):
    resTime = {}
    for line in linelist:
        if line[index] not in resTime:
            key = line[index]
            resTime[key] = 1
        else:
            resTime[line[index]] += 1
    for key, value in resTime.items():
        print(f"{key} : {value:>} 个")

statistic(lineLen[3]['lines'],1)
statistic(lineLen[4]['lines'],2)



