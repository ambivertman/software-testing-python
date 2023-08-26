import os
import re


def subFunc(match):
    prefix = match.group(1)
    number = int(match.group(2)) + 3
    dest = f'/{prefix}{number}'

    return dest


def edit(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        content = f.read()

    content = re.sub(r"/(\?p=)(\d+)", subFunc, content)
    with open(filepath,'w',encoding='utf8') as f:
        f.write(content)
    print(f"{filepath}修改成功")


# 获取所有文件路径
filelist = []
for (root, dirnames, filenames) in os.walk('./prac_re'):
    for filename in filenames:
        fpath = os.path.join(root, filename)
        filelist.append(fpath)

for file in filelist:
    edit(file)
