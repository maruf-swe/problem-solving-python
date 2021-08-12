while True:
    a, b = list(map(int, input().split()))
    if a <= 0 or b <= 0:
        break
    else:
        start = min(a, b)
        end = max(a, b)
        sum = 0
        result = ''
        for i in range(start, end + 1):
            result += str(i) + ' '
            sum += i
        result += 'Sum=%d'
        print(result % sum)
        # print(f'{result} Sum={sum}') presentation error
