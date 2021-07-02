# how to find factor of number

def factor(x):
    print("Factor of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


num = int(input())
factor(num)
