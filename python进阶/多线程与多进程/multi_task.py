import os
from threading import Thread,Lock

toolpath = "e/tools/wget.exe"

def download(toolpath, url):
    os.system(f"{toolpath} {url}")

while True:
    url = input("请输入下载地址:")
    thread = Thread(download,args=(toolpath,url))
    thread.start()
