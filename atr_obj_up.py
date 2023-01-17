class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
a.x, a.y = 1, 2
b.color = 'green'
print(a.x, a.y)
print(a.color)
print(b.x, b.y)
print(b.color)
