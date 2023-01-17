from pprint import pprint


class Point:
    x = 0
    y = 0
    z = 0
    color = 'black'

class Point1:
    pass


Point1.x = 10
setattr(Point1, 'y', 20)
Point1.z = 30
setattr(Point1, 'color', 'green')

pprint(Point.__dict__)
pprint(Point1.__dict__)
