class Point:
    pass


setattr(Point, 'color', 'black')
a = Point()
setattr(a, 'x', 0)
setattr(a, 'y', 0)
print(Point.color)
print(a.x)
print(a.y)
print(Point.x)