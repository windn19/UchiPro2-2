from pprint import pprint


class Button:
    pass


name_attr = input()
value = input()
setattr(Button, name_attr, value)
pprint(Button.__dict__)
