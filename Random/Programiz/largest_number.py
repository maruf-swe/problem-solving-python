# Python program to find the largest number among the three input numbers

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    print(f"Largest Number is {num1}")

elif num2 >= num1 and num2 >= num3:
    print(f"Largest Number is {num2}")

else:
    print(f"Largest Number is  {num3}")
