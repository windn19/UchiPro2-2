class Category:
    x = 123
    st = 'Hello'

    def __str__(self):
        return f'{self.st} --> {self.x}'



cat = Category()
# attr, value = input().split()
# setattr(cat, attr, value)
# print(cat.__dict__)
# attr = input()
# print(hasattr(cat, attr))
print(cat)