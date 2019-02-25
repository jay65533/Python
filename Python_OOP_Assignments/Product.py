class Product:
    def __init__(self,price,item_name, weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        
    def sell(self):
        self.status = "sold"
        return self.status
    
    def addTax(self, taxAmt):
        self.price = self.price * taxAmt + self.price
        return self.price

    def returnItem(self,reason_for_return):
        if(reason_for_return == "defective"):
            self.status = "defective"
            self.price = 0
        if(reason_for_return == "like new"):
            self.status = "for sale"
        if(reason_for_return == "opened"):
            self.status = "used"
            self.price = self.price - self.price*0.2
        return self
        
    def displayInfo(self):
        print("The name of the item is " + str(self.item_name))
        print("The weight is " + str(self.weight) + " pounds")
        print("The status is " + str(self.status))
        print("The price is " + str(self.price) + " dollars")

item0 = Product(1000,"Sofa",200,"Ashley-Furniture")
item0.sell()
item0.addTax(0.10)
item0.displayInfo()
print()
item1 = Product(100,"Goku Action Figure",65,"Bandai")
item1.sell()
item1.addTax(0.10)
item1.returnItem("like new")
item1.displayInfo()
print()
item2 = Product(200,"Charmander Plushie",10,"Pokemon")
item2.sell()
item2.addTax(0.10)
item2.returnItem("opened")
item2.displayInfo()
print()
item2 = Product(10,"Kingdom Hearts Poster",5,"Square-Enix")
item2.sell()
item2.addTax(0.20)
item2.returnItem("defective")
item2.displayInfo()
