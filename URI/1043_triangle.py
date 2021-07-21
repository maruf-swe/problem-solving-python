A, B, C = list(map(float, input().split()))
if (A < B + C and B < A + C and C < A + B):
    print("Perimetro = %0.1f" % (A + B + C))
else:
    print("Area = %0.1f" % ((C * (A + B)) / 2))
