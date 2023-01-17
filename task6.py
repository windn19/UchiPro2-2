from pprint import pprint


class Button:
    pass


for i in range(2):
    item = input().split()
    if item[0] == 'setattr':
        setattr(Button, item[1], item[2])
    elif item[0] == 'delattr' and hasattr(Button, item[1]):
        delattr(Button, item[1])
    pprint(Button.__dict__)
