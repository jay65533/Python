class Animal:
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
    def run(self):
        self.health = self.health - 5
    def display_health(self):
        print("The name of the animal is: " + str(self.name))
        print("The remaining health is: " + str(self.health))
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health = self.health + 5
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.health = 170
    def fly(self):
        self.health = self.health - 10
    def display_health(self):
        print("This is a dragon")
        super().display_health()
animal1 = Animal("cow")
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.display_health()
print()
animal2 = Dog("dog")
animal2.walk()
animal2.walk()
animal2.walk()
animal2.run()
animal2.run()
animal2.pet()
animal2.display_health()
print()
animal3 = Dragon("dragon")
animal3.fly()
animal3.display_health()
