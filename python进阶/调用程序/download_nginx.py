import os

version = input('请输入版本号:')
cmd = fr'e:\tools\wget http://mirrors.sohu.com/nginx/nginx-{version}.zip'
os.system(cmd)

