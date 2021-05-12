number = int(input())

def fact(number):
    if number < 0:
        return ("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
        return ("The factorial of 0 is 1")
    elif number == 1:
        return 1
    else:
        return (number * fact(number - 1))


print(fact(number))