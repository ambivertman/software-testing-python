class BenzCar:
    brand = "奔驰"
    country = "德国"

    @staticmethod
    def pressHorn():
        print("嘟嘟~~~~~~")

    def __init__(self, color, engineSN):
        self.color = color
        self.engineSN = engineSN

    def changeColor(self, newColor):
        self.color = newColor


class Benz2016(BenzCar):
    price = 580000
    model = 'Benz2016'

    def __init__(self, color, engineSN, weight):
        BenzCar.__init__(self, color, engineSN)
        self.weight = weight
        self.oilweight = 0

    def filloil(self,oilAdded):
        self.oilweight += oilAdded
        self.weight += oilAdded

class Benz2018(BenzCar):
    price = 880000
    model = 'Benz2018'
