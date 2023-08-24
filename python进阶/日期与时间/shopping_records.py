import time

with open("./esn.log","r",encoding='utf8') as f:
    content = f.readlines()

for index,line in enumerate(content):
    content[index] = line.split(">")[0]

shoppingInfo = {}
for line in content:
    date = time.strftime("%Y-%m-%d",time.localtime(eval(line)))
    if date not in shoppingInfo:
        shoppingInfo[date] = 1
    else:
        shoppingInfo[date] += 1

for k,v in shoppingInfo.items():
    print(f"{k}购物:{v}次")