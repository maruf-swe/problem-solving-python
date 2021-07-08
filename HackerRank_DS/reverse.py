def reverseArray(a):
    after_reverse = a[::-1]
    return after_reverse


arr = list(map(int, input().rstrip().split()))
res = reverseArray(arr)
print(res)
