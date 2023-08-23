with open('prac_filerw.txt', 'r', encoding='utf8') as f:
    content = f.readlines()

num = int(input("请输入像增加的数值: "))

keyword = 'https://www.bilibili.com/video/av74106411/?p='
newContent = ''

for line in content:
    pos = line.find(keyword)
    if pos < 0:
        newContent += line
    else:
        startPos = pos+len(keyword)
        endPos = startPos
        while True:
            endPos += 1
            if not line[startPos:endPos].isdigit():
                break

        endPos -= 1
        num = int(line[startPos:endPos]) + num
        newContent += line[:startPos] + str(num) + line[endPos:]

    with open('prac_filerw2.txt', "w", encoding='utf8') as f:
        f.write(newContent)