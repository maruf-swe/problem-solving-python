# with built in function
def simpleArraySum(ar):
    total = sum(ar)
    return total

  
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))

# another solution

def simpleArraySum(ar):
    total = 0
    for i in range((len(ar))):
        total += ar[i]
    return total


ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))
