class Vehicle:
    __speed = 0  # protected data member

    def __init__(self, speed=0):  # constructor
        print('constructor')
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed


car1 = Vehicle(5)
# print(car1.__speed) #AttributeError
print(car1._Vehicle__speed)  # to access protected member
car1.setSpeed(10)
print(car1.getSpeed())  
