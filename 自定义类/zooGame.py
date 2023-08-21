import random
import time


class Game():
    def __init__(self, room_list):
        self.RoomList = room_list
        self.start_time = None
        self.duration = 180

    def randRoom(self):
        room = self.RoomList[random.randint(0, len(self.RoomList) - 1)]
        return room.choose()

    def start_game(self):
        self.start_time = time.time()
        while True:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.duration:
                print("时间到！游戏结束。")
                self.end_game()
                break

            is_continue = self.randRoom()
            if is_continue:
                print(f"已经进行了 {int(elapsed_time)} 秒")

            else:
                break
    def end_game(self):
        for room in self.RoomList:
            print(f"房间号:{room.ID:>3}, 动物:{type(room.animal).__name__:>5}, 体重: {room.animal.weight}")

class Room:
    def __init__(self, ID, animal_dict):
        self.operation = None
        self.ID = ID
        animal = random.randint(1, len(animal_dict))
        self.animal = animal_dict[animal]()

    def choose(self):
        print(f"房间号: {self.ID: > 3}")
        self.operation = int(input('''请选择操作选项：
        1 喂食
        2 敲门
        0 退出
    输入:'''))
        if self.operation == 1:
            self.feed()
            return True
        elif self.operation == 2:
            self.knock()
            return True
        else:
            return True

    def feed(self):
        food = input("Enter grass or meat:")
        if food == "meat":
            if type(self.animal) is Tiger:
                self.animal.weight += 10
                print("喂对了, 体重增加10斤")
            else:
                self.animal.weight -= 10
                print("喂错了, 体重减少10斤")
        else:
            if type(self.animal) is Tiger:
                self.animal.weight -= 10
                print("喂错了, 体重减少10斤")
            else:
                self.animal.weight += 10
                print("喂对了, 体重增加10斤")

    def knock(self):
        print(f"房间号{self.ID:>3}")
        self.animal.howl()


class Animal:
    weight = 0
    barking = ''

    def howl(self):
        print(self.barking)
        self.weight -= 5


class Tiger(Animal):
    weight = 200
    barking = 'Wow!!'


class Sheep(Animal):
    weight = 100
    barking = 'mie~~'


# 创建游戏, 初始化房间
RoomList = []
animalDict = {1: Tiger, 2: Sheep}
# 房间类给定ID, 随机放入一种动物
for i in range(1, 11):
    RoomList.append(Room(i, animalDict))

game = Game(RoomList)
game.start_game()
