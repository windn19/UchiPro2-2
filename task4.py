from pprint import pprint


class Circle:
    x = 0
    y = 0
    R = 5
    color = 'black'


x = int(input())
y = int(input())
R = int(input())
color = input()
a = Circle()
a.x, a.y, a.R, a.color = x, y, R, color
print(a.__dict__)
