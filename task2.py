from pprint import pprint


class Point:
    x = 0
    y = 0
    z = 0
    color = 'black'


a = Point()
b = Point()
print(a.__dict__)
print(b.__dict__)
