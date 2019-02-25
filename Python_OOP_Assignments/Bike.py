class Bike:
    def __init__(self,price,max_speed):
        self.price = price
        self.miles = 0
        self.max_speed = max_speed
    def displayInfo(self):
        print ("The price is " + str(self.price))
        print ("The miles of the bike is " + str(self.miles))
        print ("The max speed of the bike is " + str(self.max_speed))
    def ride(self):
        print ("Riding")
        self.miles = self.miles + 10
    def reverse(self):
        if(self.miles > 0):
            print("Reversing")
            self.miles = self.miles - 5
        else:
            print("Can't reverse")
        
    
bike1 = Bike (150, 500)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike (100, 300)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike (100, 300)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()






