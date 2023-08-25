from random import randint
import time
from threading import Thread


class Game:
    def __init__(self):
        self.duration = 0
        self.rooms = None

    def generate_rooms(self):
        self.rooms = {}
        for i in range(10):
            if randint(0, 1):
                self.rooms[i + 1] = Room(Tiger(200))
            else:
                self.rooms[i + 1] = Room(Sheep(100))

    def timer(self):
        while self.duration < 120:
            self.duration += 1
            time.sleep(1)
        print("\n游戏时间到,游戏结束!")
        self.print_info()

    def start_game(self):
        while True:
            roomID = randint(1, 10)
            room = self.rooms[roomID]
            op = input(f"我们来到了房间{roomID},要敲门吗?[y/n]")
            if op == 'y':
                room.knock_room()

            food = input('请给房间里面的动物喂食:')
            room.feed_animal(food)

    def print_info(self):
        for ID, room in self.rooms.items():
            print(f"房间:{ID},{room.animal.classname},{room.animal.weight}")

    def thread_control(self):
        th1 = Thread(
            target=self.start_game,
            daemon=True
        )
        th2 = Thread(
            target=self.timer
        )
        th1.start()
        th2.start()
        th2.join()


class Room:
    def __init__(self, animal):
        self.animal = animal

    def knock_room(self):
        self.animal.howl()

    def feed_animal(self, food):
        if food == self.animal.food:
            self.animal.weight += 10
            print('正确，体重 + 10')
        else:
            self.animal.weight -= 10
            print('错误，体重 - 10')


class Animal:
    sound = None

    def __init__(self, weight):
        self.weight = weight

    def howl(self):
        print(f"{self.sound}")
        self.weight -= 5
        print("体重-5")


class Tiger(Animal):
    classname = '老虎'
    food = 'meat'
    sound = 'Wow!!'


class Sheep(Animal):
    classname = '绵羊'
    food = 'grass'
    sound = 'mie~~'


game = Game()
game.generate_rooms()
game.thread_control()