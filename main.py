class Test:
    name = 'test'


class Task:
    id = 0
    name = 'task'
    category_name = None


a = Test()
a.name = 'new'
print(a.__dict__)
# delattr(a, 'name')
if hasattr(a, 'name'):
    setattr(a, 'new_name', 'new')
else:
    delattr(a, 'name')
print(a.__dict__)
#
task = Task()
task.id = 1
task.name = 'new_task'
task.category_name = 0
print(task.__dict__)
