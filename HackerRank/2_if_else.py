#hackerrank problem 2
n = int(input().strip())
if (n % 2 == 0):
    if n in range(2, 5):
        print('Not Weird')
    elif n in range(6, 21):
        print('Weird')
    elif n > 20:
        print('Not Weird')
    else:
        print('Weird')


n = int(input())
if n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')


