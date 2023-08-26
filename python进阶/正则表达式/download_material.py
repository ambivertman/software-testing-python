import os
import re
from threading import Thread


def download(toolpath, targetpath):
    os.system(f'{toolpath} "{targetpath}"')


# 1.下载index.html
toolpath = "e:/tools/wget.exe"
targetpath = "http://www.listeningexpress.com/studioclassroom/ad/"
download(toolpath, targetpath)

with open("./index.html", "r") as f:
    content = f.read()

p = re.compile(r"p\('(?P<filename>.*?\.mp3)'\)")

threadList = []
for filename in p.findall(content):
    thread = Thread(
        target=download,
        args=(toolpath, targetpath + filename)
    )
    thread.start()
    threadList.append(thread)

for thread in threadList:
    thread.join()

print("所有文件下载完成!")
