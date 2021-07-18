X, Y = list(map(int, input().split()))
price = 0
if (X == 1):
    price = (4.00 * Y)
elif (X == 2):
    price = (4.50 * Y)
elif (X == 3):
    price = (5.00 * Y)
elif (X == 4):
    price = (2.00 * Y)
elif (X == 5):
    price = (1.50 * Y)

print("Total: R$ %.2f" % price)
