n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    x = input().split(' ')
    command = x[0]
    if command == "pop":
        s.pop()
    elif command == "discard":
        s.discard(int(x[1]))
    elif command == "remove":
        s.remove(int(x[1]))
total = sum(s)

print(total)
