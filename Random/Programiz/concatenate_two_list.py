list1 = [2, 3, 4, 5]
list2 = [1, 2, 6, 8, 5]

list3 = list1 + list2
print(list3)

# Using iterable unpacking operator *
list_1 = [1, 'a']
list_2 = range(2, 10)

list_joined = [*list_1, *list_2]
print(list_joined)

# joined with unique values

list1 = [2, 3, 4, 5]
list2 = [1, 2, 6, 8, 5]

list3 = list(set(list1 + list2))
print(list3)
