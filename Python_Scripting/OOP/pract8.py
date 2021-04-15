#Inheritance
#Animal class is the parent or base class and Mamal and Fish are Child or Sub
# Not only methods inherits the parents class but attributes also do
#As an example, we set up a constructor __init__ and define the attribute age



class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
m.age= 10
print(m.age)
print(isinstance(m, Mammal))
#Every class inherits from the class called object
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
