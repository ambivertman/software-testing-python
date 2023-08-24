from subprocess import PIPE, Popen
import os

toolPath = 'E:/tools/ffmpeg.exe'
targetDir = './callOthers/'
targetFiles = []
for root, dirNames, filenames in os.walk(targetDir):
    for filename in filenames:
        targetFiles.append(root + filename)

for file in targetFiles:
    proc = Popen(
        f'''{toolPath} -i "{file}" -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy "{file.replace("mp4", "new.mp4")}"''',
        shell=True)


