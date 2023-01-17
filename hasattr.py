class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
a.size = 10
print(hasattr(Point, 'color'))
print(hasattr(Point, 'size'))
print(hasattr(a, 'size'))
