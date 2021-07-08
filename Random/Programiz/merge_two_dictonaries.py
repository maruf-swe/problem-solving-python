# Using operator |
dict_1 = {1: 'a', 2: 'e'}
dict_2 = {2: 'd', 4: 'd'}

print(dict_1 | dict_2)

# Using operator **
dict_1 = {1: 'a', 2: 'x'}
dict_2 = {2: 'k', 4: 'd'}

print({**dict_1, **dict_2})

# Using copy() and update()
dict_1 = {1: 'a', 2: 'x'}
dict_2 = {2: 'k', 4: 'd'}
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)
