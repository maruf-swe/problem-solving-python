# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
# int A[n]: the array to reverse

def reverseArray(a):
    after_reverse = a[::-1]
    return after_reverse


arr = list(map(int, input().rstrip().split()))
res = reverseArray(arr)
print(res)
