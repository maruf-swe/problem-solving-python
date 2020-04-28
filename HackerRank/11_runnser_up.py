''''find who is runners up

n=int(input())
arr = map(int, input().split())
newlist = []
for i in arr:
    if i not in newlist:
        newlist.append(i)
newlist.sort(reverse=False)
print(newlist[-2])
'''

n = int(input())

nums = map(int, input().split())
print(sorted(list(set(nums)))[-2])