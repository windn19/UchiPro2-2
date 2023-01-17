class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
print(getattr(Point, 'color'))
print(getattr(Point, 'color', 'Нет такого атрибута'))
print(getattr(Point, 'size', 'Нет такого атрибута'))
print(getattr(a, 'color', 'Нет такого атрибута'))
print(getattr(a, 'size'))
