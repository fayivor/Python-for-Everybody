class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point =Point(1,2)
other = Point(1,2)
print(point == other)

#This prints out False since by default the equality operator compares the references
#or addresses of these two objects in memory. These two variables are referencing
# two different objects in memory.
# To solve this problem we need a magic method as seen in Pract4.py
