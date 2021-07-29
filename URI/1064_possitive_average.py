count = 0
sum = 0
for i in range(6):
    value = float(input())
    if value > 0:
        count += 1
        sum += value

print(count, "valores positivos")
print("%0.1f" % (sum / count))

"""
7
-5
6
-3.4
4.6
12"""
