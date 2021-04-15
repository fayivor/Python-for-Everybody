class Point:
    default_color = "green"

    def __init__(self, x, y):
        self.x = x
        self.y = y
    #another magic method
    def __str__(self):
        return f"({self.x}, {self.y})"



    #creating a class method called decorator
    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw (self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1,2)
#The __str__ magic method converts the instance object to a string instead of
# printing out the main memory location without it
#So init and str are two useful magic methods in python
print("point obj is", str(point))
vv= point.zero()
print("vv",vv)
print(point.default_color)
point.default_color ="red"
print(point.default_color)
print(Point.default_color)
point.draw()
another = Point(3,4)
another.draw()
