n = int(input())
for i in range(n):
    val1, val2, val3 = list(map(float, input().split()))
    avg = ((val1 * 2) + (val2 * 3) + (val3 * 5)) / 10
    print(f'{avg:.1f}')
