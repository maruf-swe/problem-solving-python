# Count Number of Digits in an Integer using while loop

num = int(input())
count = 0
while num != 0:
    num //= 10
    count += 1

print("Number of digits: ", count)
