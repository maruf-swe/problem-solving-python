n = int(input())
for i in range(n):
    val = int(input())
    if val < 0:
        if val % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif val > 0:
        if val % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif val == 0:
        print("NULL")
