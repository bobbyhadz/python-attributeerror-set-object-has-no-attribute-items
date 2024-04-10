# AttributeError: 'set' object has no attribute 'items'

# Separate the keys and values of the object with colons

employee = {'name': 'Bobby Hadz', 'age': 30}

# 👇️ <class 'dict'>
print(type(employee))


# 👇️ dict_items([('name', 'Bobby Hadz'), ('age', 30)])
print(employee.items())

for k, v in employee.items():
    print(k, v)