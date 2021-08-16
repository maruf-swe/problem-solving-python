while True:
    x, y = list(map(int, input().split()))
    if x == y:
        break
    else:
        if x > y:
            print("Decrescente")
        else:
            print("Crescente")
