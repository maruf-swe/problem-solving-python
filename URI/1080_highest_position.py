highest = 0
position = 0
for i in range(1, 101):
    value = int(input())
    if value > highest:
        highest = value
        position = i

print(highest)
print(position)
