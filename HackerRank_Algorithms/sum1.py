def simpleArraySum(ar):
    total = sum(ar)
    return total

  
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))
