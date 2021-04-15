#Method Overriding means replacing the method defined in a base class
# in this cases we extended or replaced the __init__ method we have defined in these
# Animal class so using the super() method prevents the overriding of the
#method in Animal class

class Animal:
    def __init__(self):
        print("Animal COnstructor")
        self.age = 1
    def eat(self):
        print("eat")
class Mammal(Animal):

    def __init__(self):

        print("Mammal Constructor")
        self.weight = 3
        super().__init__()
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(m.weight)
print(m.age)
m.age= 10
print(m.age)
print(isinstance(m, Mammal))
#Every class inherits from the class called object
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
