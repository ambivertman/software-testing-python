with open('./0019.txt','rb') as f:
    content = f.read().splitlines()

for index,line in enumerate(content):
    try:
        line = line.decode('utf8')
        print(f"第{index:05}行, 有{len(line)}个字符")
    except:
        print(f"第{index:05}行, 有非utf8编码字符!!!!")