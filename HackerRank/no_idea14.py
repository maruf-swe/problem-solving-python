n,m = map(int,input().split())
l = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
happiness = 0

for i in l:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)


another solutin
n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0
for elem in array:
    happiness += elem in a
    happiness -= elem in b
print(happiness)
