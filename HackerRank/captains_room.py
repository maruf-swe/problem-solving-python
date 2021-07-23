k, rooms = input(), input().split()
single, multiple = set(), set()
for room in rooms:
    if room in single:
        multiple.add(room)
    else:
        single.add(room)

print(single.difference(multiple).pop())


'''
l = map(int, raw_input().split())
for value in set(l):
    if l.count(value) == 1:
        print value
 timeout for some testcases.'''