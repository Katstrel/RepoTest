# Rebecca classes.py | Case Study with Classes

class Vehicle():
    def __init__(this, type):
        this.typeclass = type

class Automobile(Vehicle):
    def __init__(this, type):
        super().__init__(type)
        this.year = input('Please Input the Year of Model: ')
        this.make = input('Please Input the Make of Model: ')
        this.model = input('Please Input the Model: ')
        this.doors = input('Please Input the Number of Doors: ')
        this.roof = input('Please Input the Roof Type: ')

choice = input('Type Number to Choose Vehicle Type:\n1) Car\n')
if choice == "1":
    userCar = Automobile("Car")
    print('Vehicle Type:', userCar.typeclass)
    print('Year:', userCar.year)
    print('Make:', userCar.make)
    print('Model:', userCar.model)
    print('Number of Doors:', userCar.doors)
    print('Type of Roof:', userCar.roof)