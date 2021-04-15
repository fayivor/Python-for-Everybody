class Point:
    default_color = "green"

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw (self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1,2)
point = Point.zero()
print(point)
print(point.default_color)
point.default_color ="red"
print(point.default_color)
print(Point.default_color)
point.draw()
another = Point(3,4)
another.draw()
