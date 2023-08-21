import sys
sys.path.append('E:/231软件测试实战课/模块和库/文件')
from phone.apple.iphone6 import askPrice as iPhone6
from phone.apple.iphone7 import askPrice as iPhone7
from phone.samsung.note.galaxy_note8 import askPrice as note8
from phone.samsung.s.galaxy_s7 import askPrice as s7


iPhone6()
iPhone7()
note8()
s7()