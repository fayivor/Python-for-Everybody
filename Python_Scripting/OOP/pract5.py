class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,self.y +other.y)



point =Point(1,2)
other = Point(11,21)
point1 =Point(10,5)
other2 = Point(1,23)
new_add = point + other
print(point + other)
print("new add=", (new_add.x,new_add.y))
new_add12 = point1 + other2
print(point1 + other2)
print("new_add12 =", (new_add12.x,new_add12.y))
#magic methods for adding two instances or objects
