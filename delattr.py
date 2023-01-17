from pprint import pprint


class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
a.size = 10
del a.size
delattr(Point, 'color')
print(a.__dict__)
pprint(Point.__dict__)
del a.size
