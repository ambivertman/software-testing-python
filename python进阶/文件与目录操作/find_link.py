import os

def replace(filepath,keyword,num):
    with open(filepath, 'r', encoding='utf8') as f:
        content = f.readlines()
    newContent = ""
    for line in content:
        pos = line.find(keyword)
        if pos < 0:
            newContent += line
        else:
            startPos = line.find(keyword)+len(keyword)
            endPos = startPos
            while True:
                endPos += 1
                if not line[startPos:endPos].isdigit():
                    break
            endPos -= 1
            num = int(line[startPos:endPos]) + num
            newContent += line[:startPos] + str(num) + line[endPos:]
    with open(filepath,'w',encoding='utf8') as f:
        f.write(newContent)

targetDir = "./prac_re"
keyword= "https://www.bilibili.com/video/av74106411/?p="
num = 3
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for filename in filenames:
        fpath = os.path.join(dirpath,filename)
        replace(fpath,keyword, num)
        print(f'{filename}修改完成')