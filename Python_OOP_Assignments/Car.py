class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
    
    def displayInfo(self):
        print ("Price: " + str(self.price))
        print ("Speed: " + str(self.speed)+"mph")
        print ("Fuel: " + str(self.fuel))
        print ("Mileage: " + str(self.mileage))
        print ("Tax:" + str(self.tax))

car1 = Car (10000,35,"Full",15)
car1.displayInfo()
print()
car1 = Car (20000,65,"Not Full",25)
car1.displayInfo()
print()
car1 = Car (1000,15,"Not Full",13)
car1.displayInfo()
print()
car1 = Car (50000,45,"Full",45)
car1.displayInfo()
print()
car1 = Car (16000,65,"Not Full",20)
car1.displayInfo()
print()
car1 = Car (7000,35,"Full",15)
car1.displayInfo()