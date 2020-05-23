n = int(input())

arr = list(map(int, input().rstrip().split()))
reverse = arr[::-1]
after_reverse = ''
for i in range(len(reverse)):
    after_reverse += str(reverse[i]) + ' '
print(after_reverse)
