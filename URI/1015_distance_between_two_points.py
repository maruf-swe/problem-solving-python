x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance = dis ** .5
print("%.4f" % distance)


# another solution
import math  # in the top possition

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("%0.4f" % distance)
