class Computer:
    def __init__(self):
        self.__maxPrice = 900
    def sell(self):
        print("Price: {}".format(self.__maxPrice))
    def setMaxPrice(self,price):
        self.__maxPrice = 1000
comp = Computer()
comp.sell()

comp.__maxPrice = 1000
comp.sell()

comp.setMaxPrice(1000)
comp.sell()
    