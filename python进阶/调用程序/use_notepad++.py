import os
from subprocess import PIPE,Popen
import time
# 打开notepad++,并打开当前的程序
cwp = os.getcwd()+r'\use_notepad++.py'
notepadPath = r"D:\Programs\Notepad++\notepad++.exe"
cmd = f"{notepadPath} {cwp}"
# os.system(cmd) 使用os.system()打开notepad++后进程会卡在这里
Popen(cmd,shell=True)
time.sleep(10)




# 寻找进程号
proc = Popen(
    'tasklist',
    stdin=None,
    stdout=PIPE,
    stderr=None,
    shell=True
    )

outinfo,errinfo = proc.communicate()
outinfo = outinfo.decode('gbk')

print(outinfo)

procs = outinfo.splitlines()
for item in procs:
    if "notepad++.exe" in item:
        print(item)
        info = item.split(' ')
        info = list(filter(None,info))
        #print(info)
        PID = info[1]
        cmd = f"Taskkill /PID {PID} /F"
        os.system(cmd)
        break


