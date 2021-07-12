def simpleArraySum(ar):
    total = sum(ar)
    return total

ar_c = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))


#another solution

def simpleArraySum(ar):
    total = 0
    for i in range((len(ar))):
        total += ar[i]
    return total


ar_c = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))
