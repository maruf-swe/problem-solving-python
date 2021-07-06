# Function to print binary number using recursion
'''This program works only for whole numbers. 
It doesn't work for real numbers having fractional values such as: 25.5, 45.64'''


def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end='')


dec = 34

convertToBinary(dec)
print()
