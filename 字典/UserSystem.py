from pprint import pprint

members = {
    1: {'name': '白月黑羽', 'level': 3, 'coins': 300},
    2: {'name': '短笛魔王', 'level': 5, 'coins': 330},
    3: {'name': '紫气一元', 'level': 6, 'coins': 340},
    4: {'name': '拜月主', 'level': 3, 'coins': 32200},
    5: {'name': '诸法空', 'level': 4, 'coins': 330},
    6: {'name': '暗光城主', 'level': 3, 'coins': 320},
    7: {'name': '心魔尊', 'level': 3, 'coins': 2300},
    8: {'name': '日月童子', 'level': 8, 'coins': 3450},
    9: {'name': '不死尸王', 'level': 3, 'coins': 324},
    10: {'name': '天池剑尊', 'level': 9, 'coins': 13100},
}

# 通过userName查找
name2info = {}
for key, value in members.items():
    # 这样的方式,每次每次查找都需要生成一个列表, 然后线性查找
    #     if value['name'] == val:
    #         return key
    # else:
    #     print("value not found")
    name = value['name']
    value['id'] = key
    name2info[name] = value


# 检查某个userName是否为新userName, 是 True ,否 False
def checkUserName(name2info):
    name = input('请输入查找的用户账号:')
    if name not in name2info:
        print(f'对不起，账号 {name} 不存在.')
        return False

    info = name2info[name]
    print(f'账号: {name} , ID : {info["id"]} , 等级：{info["level"]} , 金币：{info["coins"]} ')

    # 与上面的代码有同样的问题, 资源资源浪费
    # for value in members.values():
    #     if value['name'] == userName:
    #         return False
    #     else:
    #         continue
    # else:
    #     return True


# 生成以name为key的字典后, 工作量大幅减少, 原来查询需要先查找到key再输出信息,现在只需要一个函数即可实现

# 输入用户名, 返回用户信息
# def userInfo(members):
#     global userName
#     while (True):
#         userName = input("请输入账号名:")
#         if not checkUserName(members, userName):
#             key = return_key(members, userName)
#             print(f"ID:{key:>3}, level: {members[key]['level']:>3}, coins:{members[key]['coins']:>6}")
#             break
#         else:
#             print("该账号名不存在")

# 输入用户名, 检查是否可用, 若可行则增加用户, 否则提示重新输入
def addUser(name2info):
    while (True):
        userName = input("请输入账号名:")
        if userName not in name2info:
            print('对不起，该账号已经存在')
        else:
            break
    while True:
        level = input('请输入该用户的等级:')
        # 如果不是数字 ， 则输入格式错误
        if not level.isdigit():
            print('对不起，等级必须为一个数字')
        else:
            level = int(level)  # 转化为整数
            break

    while True:
        coins = input('请输入该用户的金币数量:')
        # 如果不是数字 ， 则输入格式错误
        if not coins.isdigit():
            print('对不起，金币数 必须为一个数字')
        else:
            coins = int(coins)  # 转化为整数
            break

    # 要产生一个不存在的ID号， 这里我们取 当前最大的ID号+ 1
    newId = max(members.keys()) + 1
    # 注意： 两个字典里面都要添加
    members[newId] = {'name': userName, 'level': level, 'coins': coins}
    name2info[name] = {'name': userName, 'level': level, 'coins': coins, 'id': newId}


# 定义删除用户账号的处理函数
def delAccount():
    name = input('请输入要删除的用户账号:')
    if name not in name2info:
        print(f'对不起，账号 {name} 不存在.')
        return

    # 注意： 两个字典里面都要删除
    theID = name2info[name]['id']
    name2info.pop(name)
    members.pop(theID)


# 定义打印表内容的处理函数
def showTables():
    print('\n现在name2info的表内容是：\n')
    pprint(name2info)
    print('\n现在members的表内容是：\n')
    pprint(members)


menu = '''
请选择操作选项：
   1 查看用户账号信息
   2 添加用户
   3 删除用户
   4 列出所有用户信息
   0 退出
'''
# 显示主菜单
while True:
    choice = input(menu)

    # 选择查看查看用户账号
    if choice == '1':
        checkUserName(name2info)
    elif choice == '2':
        addUser(name2info)
    elif choice == '3':
        delAccount()
    elif choice == '4':
        showTables()
    elif choice == '0':
        break
