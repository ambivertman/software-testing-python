from random import randint
import time


# 软件中类的设计结构
# - 游戏类
#     - 玩家类
#         - 战士类
#
#     - 森林类
#         - 妖怪类


class Player:
    def __init__(self, wealth):
        self.wealth = wealth
        self.warriors = {}
    # 雇佣战士
    def hire_warrior(self, WarriorType):
        if self.wealth - WarriorType.price < 0:
            print(f"灵石余额不足,当前余额:{self.wealth}")
            return
        while True:
            name = input("请为战士命名:")
            name = name.strip()
            if name == '' or len(name) > 10:
                print("昵称不合法,请重新输入!")
                continue
            if name in self.warriors:
                print("该名称已被使用,请重新输入!")
                continue
            else:
                break

        self.wealth -= WarriorType.price
        self.warriors[name] = WarriorType(name)
        print(f"{name}已加入队伍")

    def hire(self):
        hireMenu = '''
请输入你想要雇佣的战士:
1.弓箭手
2.斧头兵
3.退出
输入:'''
        while True:
            choice = input(hireMenu)
            if choice not in ['1', '2', '3']:
                print("请输入正确的命令")
                continue

            if choice == '3':
                break

            if choice == '1':
                self.hire_warrior(Archer)
            else:
                self.hire_warrior(Axeman)

    def choose_warrior(self, name):
        return self.warriors[name]
    #治愈自己的战士
    def heal(self, name, count):
        if self.wealth < count:
            print('剩余灵石不足')
            return

        self.warriors[name].HP += count
        if self.warriors[name].HP > self.warriors[name].maxHP:
            self.warriors[name].HP += self.warriors[name].maxHP
        self.wealth -= count
    # 输出玩家信息
    def printInfo(self):
        print('\n您麾下战士情况如下')
        for name, warrior in self.warriors.items():
            print(f'{name}: {warrior.typeName} 生命值 {warrior.HP}')

        print(f'您的灵石还剩余{self.wealth}')


class Warrior:
    price = None
    maxHP = None
    ATK = None

    def __init__(self, name):
        self.name = name
        self.HP = self.maxHP

    def battle(self, monster):
        self.HP -= self.ATK[monster.typeName]


class Archer(Warrior):
    typeName = '弓箭手'
    price = 100
    maxHP = 100
    ATK = {'鹰妖': 20, '狼妖': 80}


class Axeman(Warrior):
    typeName = '斧头兵'
    price = 120
    maxHP = 120
    ATK = {'鹰妖': 80, '狼妖': 20}


class Eagle:
    typeName = '鹰妖'


class Wolf:
    typeName = '狼妖'


class Forest:
    def __init__(self, monsterDict):
        self.monster = monsterDict[randint(1, len(monsterDict))]


class Game():
    monsterDict = {1: Eagle, 2: Wolf}

    def __init__(self):
        self.player = Player(1000)
        self.forests = []

    # 生成含有随机妖怪的森林
    def generate_forests(self):
        for i in range(7):
            self.forests.append(Forest(self.monsterDict))
        print("本次游戏森林中的怪物是:")
        for forest in self.forests:
            print(forest.monster.typeName)
        time.sleep(5)
        print('\n' * 20)
    #玩家招募战士
    def player_build_team(self):
        self.player.hire()
        print("队伍组建完成,挑战开始!")
    #游戏主体
    def challenge(self):
        for forestNo, forest in enumerate(self.forests):
            while True:
                while True:
                    name = input("输入出战战士的名称:")
                    name = name.strip()
                    if name not in self.player.warriors:
                        print("该战士不存在,请重新输入!")
                        continue
                    break

                warrior = self.player.choose_warrior(name)
                print(f'当前森林里面是 {forest.monster.typeName}')
                warrior.battle(forest.monster)
                if warrior.HP <= 0:
                    print(f"{warrior.name}已牺牲,请派出另外一名战士!")
                    self.player.warriors.pop(name)
                    continue
                else:
                    break

            while True:
                self.player.printInfo()
                is_Continue = input('''是否治疗?
1.治疗
2.退出
输入:''')
                if is_Continue == '1':
                    pass
                else:
                    break
                while True:

                    op = input('''\n请输入疗伤战士名字和灵石数量，格式如为：姓名+20\n输入:''')
                    if '+' not in op:
                        print("格式错误,请重新输入!")
                        continue
                    else:
                        name, count = op.split('+')
                        count = int(count)
                        self.player.heal(name, count)
                        break



game = Game()
game.generate_forests()
game.player_build_team()
game.challenge()
