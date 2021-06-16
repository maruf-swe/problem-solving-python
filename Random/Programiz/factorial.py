# Python program to find the factorial of a number provided by the user.

num = int(input())

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
    
    
# another solution

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Sorry, factorial does not exist for negative numbers")

    return n * factorial(n - 1)


num = 5
print("Factorial of", num, "is",factorial(num))


