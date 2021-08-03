n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    start = min(a, b)
    end = max(a, b)
    sum = 0
    for j in range(start + 1, end):
        if j % 2 == 1:
            sum += j
    print(sum)
