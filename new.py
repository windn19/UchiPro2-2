class Category:
   pass


cat = Category()
attr, value = input().split()
setattr(cat, attr, value)
attr = input()
print(hasattr(cat, attr))