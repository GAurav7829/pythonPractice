class Vehicle:
    speed = 0

#    def __new__(cls):
#        print('cons')
#        return object.__new__(cls)

    def __init__(self, speed=0):    #constructor
        print('constructor')
        self.speed = speed
    
    def __del__(self):
        print('destructor called')

    def increaseSpeed(self, increaseAmount):
        self.speed += increaseAmount
    
    def __add__(self, otherVehicle):
        return Vehicle(self.speed + otherVehicle.speed)

class Car(Vehicle): #Car inherit Vehicle class
    weight = 10

    def increaseWeight(self, weight):
        self.weight += weight
    
    def increaseSpeed(self, increaseAmount):    #override method
        print('Override method call...')
        self.speed *= increaseAmount


car1 = Vehicle()
car2 = Vehicle(10)

childCar = Car(2)   #as Vehicle class has constructor method with parameter

print('Car1 speed: %i' %car1.speed)
car1.increaseSpeed(5)
print('Car1 speed: %i' %car1.speed)

print('Car2 speed: %i' %car2.speed)

car3 = car1 + car2
print('Car3 speed: %i' %car3.speed)

print('Child car initial weight: ', childCar.weight)
childCar.increaseWeight(10)
print('child car updated weight: ', childCar.weight)
childCar.increaseSpeed(7)
print('child car speed', childCar.speed)

del car1    #destroying object
del car2