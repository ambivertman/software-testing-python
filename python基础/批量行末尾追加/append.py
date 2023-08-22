with open('prac_filerw.txt', 'r', encoding='utf8') as f:
    content = f.read()
linelist = list(filter(None,content.splitlines()))
num = int(input("请输入像增加的数值: "))
for index, line in enumerate(linelist):
    # 找到含有链接的行
    if "https" in line:
        # 记录'p='后面有几位数字
        count = 0
        start = line.find("p=") + 2
        for char in line[start:]:
            if char.isdigit():
                count += 1
            else:
                break
            # 将等号后的count位转换为数值+3
        originalNum = line[start:start + count]
        replaceNum = eval(originalNum) + num
        linelist[index] = line.replace(f"p={originalNum}",f"p={str(replaceNum)}")

with open("prac_filerw.txt", 'w', encoding="utf8") as f:
    f.write('\n'.join(linelist))

