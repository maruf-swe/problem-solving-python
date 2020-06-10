def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False

    return True


n = int(input())
for i in range(n):
    num = int(input())
    if isPrime(num):
        print("Prime")
    else:
        print("Not prime")


def solve(num):  # time limit error
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                print("Not prime")
                break
        else:
            print("Prime")

    else:
        print("Not prime")


n = int(input())
for i in range(n):
    a = solve(int(input()))

n = int(input())  # time limit error
for i in range(n):
    num = int(input())
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                print("Not prime")
                break
        else:
            print("Prime")

    else:
        print("Not prime")
