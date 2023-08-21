import random
import time


class Player:
    wealth = 1000
    forestList = []
    warriorDict = {}

    def __init__(self, monsterDict):
        # 生成随机的森林
        for i in range(7):
            self.forestList.append(Forest(monsterDict))

        for index, forest in enumerate(self.forestList):
            print(f"forest {index + 1} : {forest.monster}")
        time.sleep(5)
        print("\n" * 20 + "游戏开始!")
        # 雇佣战士
        archer_num = int(input("请输入你想要的弓箭手数目:"))
        for i in range(archer_num):
            name = input(f"请为{i + 1}号弓箭手命名:")
            self.warriorDict[name] = Archer(name)
            self.wealth -= 100

        axeman_num = int(input("请输入你想要的斧头兵数目:"))
        for i in range(axeman_num):
            name = input(f"请为{i + 1}号斧头兵命名:")
            self.warriorDict[name] = Axeman(name)
            self.wealth -= 12

    def challenge(self):
        for index, forest in enumerate(self.forestList):
            # 字典不为空继续挑战, 反之说明所有战士全部阵亡即挑战失败
            if self.warriorDict:
                warrior = self.battle(index + 1, forest)
                self.rest(warrior)
            else:
                print("挑战失败")
        print(f"挑战成功,灵石剩余数量:{self.wealth}")

    # index 是森林序号, 用于提示玩家当前所处关卡
    def battle(self, index, forest):
        while True:
            warrior = self.choose_warrior(index)
            if warrior.HP - warrior.ATK[forest.monster] >= 0:
                warrior.HP -= warrior.ATK[forest.monster]
                print(f"胜利! {warrior.name} HP : {warrior.HP}")
                return warrior
            else:
                print(f"{warrior.name} HP : {warrior.HP}, 该战士已阵亡.")
                self.warriorDict.pop(warrior.name)

    def choose_warrior(self, index):
        name = input(f"{index}号森林,请选择出战的战士的昵称:")
        warrior = self.warriorDict[name]
        return warrior

    def rest(self, warrior):
        rest = eval(input('''是否补给:
    1. 是
    0. 继续挑战
输入:'''))
        if rest:
            if self.wealth > 0:
                supplement = int(input("请输入补给的数量:"))
                if self.wealth - supplement < 0:
                    print("灵石不足!已进入下一个森林!")
                else:
                    print(f"补给成功!{warrior.name} HP : {warrior.HP}")
            else:
                print("灵石不足!已进入下一个森林!")


class Warrior:
    name = None
    price = None
    HP = None
    ATK = {}


class Archer(Warrior):
    def __init__(self, name):
        self.name = name
        self.price = 100
        self.HP = 100
        self.ATK = {'鹰妖': 20, '狼妖': 80}


class Axeman(Warrior):
    def __init__(self, name):
        self.name = name
        self.price = 120
        self.HP = 120
        self.ATK = {'鹰妖': 80, '狼妖': 20}


class Forest:
    monster = None

    def __init__(self, monsterDict):
        self.monster = monsterDict[random.randint(1, len(monsterDict))]


monsterDict = {1: "狼妖", 2: "鹰妖"}
player = Player(monsterDict)
player.challenge()
