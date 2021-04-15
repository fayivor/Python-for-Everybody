"""In object-oriented programming, the concept of inheritance allows
you to build relationships between objects, grouping together similar
concepts and reducing code duplication."""


class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
