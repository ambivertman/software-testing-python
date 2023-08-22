with open('stock.txt', 'r', encoding='utf8') as f:
    content = f.read()
    content = content.splitlines()
#将原始文件分割为"股票名称": 股票代码后存入字典
name2info = {}
code2info = {}
for line in content:
    line = line.split('|')
    # stock_dict[line[0].strip()] = line[1].strip()
    #优化, 可以建立股票代码与股票名称互相查询的字典
    name = line[0].strip()
    code = line[1].strip()
    name2info[name] = f"{name}:{code}"
    code2info[code] = f"{code}:{name}"

while(True):
    target = input("请输入股票代码或者股票名称:")
    target.strip()
    if not target:
        continue

    if target.isdigit():
        if len(target) < 6:
            print("请写全6位股票代码")
            continue
        elif target in code2info:
            print(code2info[target])
            break
        else:
            print("Not Found")
    else:
        if target in name2info:
            print(name2info[target])
        else:
            print("Not found")
    isContinue = eval(input("输入0退出查询,1继续:"))
    if not isContinue:
        break