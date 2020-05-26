n = int(input())
numOfDigit = [len(num) for num in bin(n)[2:].split('0')]
print(max(numOfDigit))
