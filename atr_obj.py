class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
a.color = 'yellow'
print(a.__dict__)
print(a.color)
print(b.color)
