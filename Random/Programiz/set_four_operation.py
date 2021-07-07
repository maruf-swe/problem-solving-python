value1 = {0, 2, 4, 6, 8}
value2 = {1, 2, 3, 4, 5}

print("Union of E and N is", value1 | value2)
print("Union of E and N is", value1.union(value2))

print("Intersection of E and N is", value1 & value2)
print("Intersection of E and N is", value1.intersection(value2))

print("Difference of E and N is", value1 - value2)
print("Difference of E and N is", value1.difference(value2))

print("Symmetric difference of E and N is", value1 ^ value2)
print("Symmetric difference of E and N is", value1.symmetric_difference(value2))
