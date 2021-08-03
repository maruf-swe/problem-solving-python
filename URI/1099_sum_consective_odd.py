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


n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    d = 0
    if (a == b):
        print(0)
    else:
        c = 0
        if (a > b):
            c = a
            a = b
            b = c
        for j in range(a + 1, b, 1):
            if (j % 2 != 0):
                d += j
        print(d)
