with open('./cfiles/gbk编码.txt', 'r', encoding='gbk') as f1:
    content1 = f1.read()

with open('./cfiles/utf8编码.txt', encoding='utf8') as f2:
    content2 = f2.read()

output = f"{content1}\n{content2}"
filename = input("请输入新文件的名称:")
with open(f"{filename}.txt", 'w', encoding='utf8') as f:
    f.write(output)
