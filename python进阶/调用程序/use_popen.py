from subprocess import PIPE, Popen

proc = Popen(
    'fsutil volume diskfree c:',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True
)
outinfo, errinfo, = proc.communicate()

outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')

print(outinfo)
print('-'*8)
print(errinfo)

outputlist = outinfo.splitlines()

free = int(outputlist[0].split(':')[1].replace(',','').split('(')[0].strip())

total = int(outputlist[1].split(':')[1].replace(',','').split('(')[0].strip())

if(free/total < 0.1):
    print("剩余空间不足")
else:
    print("剩余空间充足")


