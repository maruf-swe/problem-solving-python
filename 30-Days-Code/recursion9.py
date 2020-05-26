def factorial(n):
    fact = 0
    for i in range(1, n+1):
        fact = fact * i
    return fact

n = int(input())
result = factorial(n)
print(result)