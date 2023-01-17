from pprint import pprint


class Circle:
    x = 0
    y = 0
    R = 5
    color = 'black'


a = Circle()
a.color = 'red'
a.R = 10
pprint(a.__dict__)
pprint(Circle.__dict__)