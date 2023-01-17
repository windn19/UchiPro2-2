from pprint import pprint


class Point:
    x = 0
    y = 0
    color = 'black'


Point.color = 'red'
Point.size = 5
pprint(Point.__dict__)
