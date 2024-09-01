class Animal:
    type = "Animal"
class Pet(Animal):
    location = "Household"
class Dog(Pet):
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
print(d.type)
print(d.location)
d.bark()
