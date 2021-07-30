x = int(input())
count = 0
while True:
    if x % 2 == 1:
        print(x)
        count += 1
    x += 1
    if count == 6:
        break

