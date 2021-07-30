x = int(input())
count = 0
while True:
    if x % 2 == 1:
        print(x)
        count += 1
    x += 1
    if count == 6:
        break

# another solution
x = int(input())
i = 0
while (i < 6):
    if (x % 2 == 1):
        print(x)
        i = i + 1
    x += 1
