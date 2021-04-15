class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self,other):
        return self.x > other.x and self.y > other.y



point =Point(1,2)
other = Point(1,2)
point1 =Point(10,5)
other2 = Point(1,23)
print(point)
print(other)
print(point == other)
print(point1 > other2)

#This prints out False since by default the equality operator compares the references
#or addresses of these two objects in memory. These two variables are referencing
# two different objects in memory.
# To solve this problem we need a magic method as seen in Pract4.py
