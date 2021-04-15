'''
In addition to the __init__ constructor special method, there is also the
__str__ special method. This method allows us to define how an instance of an
object will be printed when it’s passed to the print() function. If an object
doesn’t have this special method defined, it will wind up using the default
representation, which will print the position of the object in memory.
Not super useful. Here is our Apple class, with the __str__ method added:
'''



class Apple:
  def __init__(self, color, flavor):
     self.color = color
     self.flavor = flavor
  def __str__(self):
    return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)
