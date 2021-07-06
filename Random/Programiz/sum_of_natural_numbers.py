# Python program to find the sum of natural using recursive function
def recursion_sum(value):
    if value <= 1:
        return value
    else:
        return value + recursion_sum(value - 1)


value = int(input("Enter a possitive number: "))
if value < 0:
    print("Enter a possitive Numer and Try Again: ")
else:
    print("The sum is", recursion_sum(value))
