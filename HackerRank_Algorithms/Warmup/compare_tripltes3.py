def compareTriplets(a, b):
    a_point = 0
    b_point = 0
    for i in range(3):
        if a[i] > b[i]:
            a_point += 1
        elif a[i] < b[i]:
            b_point += 1
    return a_point, b_point


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(result)


def compareTriplets(a, b):
    a_point = 0
    b_point = 0
    for i in range(int(input("How much length data you have: "))):  # for user input occures runtime error
        if a[i] > b[i]:
            a_point += 1
        elif b[i] > a[i]:
            b_point += 1
    return a_point, b_point


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(result)
