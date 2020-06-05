n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numOfSwap = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numOfSwap += 1

    if numOfSwap == 0:
        break

print("Array is sorted in {} swaps.".format(numOfSwap))
print("First Element:", (a[0]))
print("Last Element:", a[-1])
