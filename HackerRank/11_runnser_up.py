nums = map(int, input().split())
print(sorted(list(set(nums)))[-2])


print("Optional Solution")
arr = list(map(int, input().split()))
newlist = []
for i in arr:
    if i not in newlist:
        newlist.append(i)
newlist.sort(reverse=False)
print(newlist[-2])
