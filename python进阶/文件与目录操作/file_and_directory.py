import os
import shutil
import glob

# #创建 如下的目录层级结构
# os.makedirs('./backup/new/',exist_ok=True)
# #拷贝到 backup/new/source 目录里面去
# shutil.copytree('./source','./backup/new/source')
# #计算出 下载的source目录里面（不包含子目录）所有的文件的大小之和
all_files_size = 0
targetDir = './source'
for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for filename in filenames:
        fpath = os.path.join(dirpath,filename)
        all_files_size += os.path.getsize(fpath)
print(all_files_size)

bmp_files = glob.glob(f"{targetDir}/**",recursive=True)
for file in bmp_files:
    if 'bmp' in file:
        os.remove(file)
    elif 'avi' in file:
        newname = file.replace('avi','dll')
        os.rename(file,newname)
print(glob.glob(f"{targetDir}/**",recursive=True))