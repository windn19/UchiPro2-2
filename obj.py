class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
print(a.__dict__)
print(b.__dict__)
b.x = 10
b.x = b.x + 1
print(b.x)
print(b.__dict__)
Point.x = 1
c = Point()
print(a.x)
print(c.x)
