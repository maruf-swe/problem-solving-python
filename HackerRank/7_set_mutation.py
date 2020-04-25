input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split()))
print(sum(map(int, L)))


'''
m = int(raw_input())
A = set(map(int, raw_input().split(" ")))
n = int(raw_input())

for i in range(n):
    cmd, args = raw_input().split(" ")
    B = set(map(int, raw_input().split(" ")))
    eval('A.'+cmd+'(B)')

print sum(A)
'''
'''
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))
'''
'''
(_, A) = (
    raw_input(),
    set(map(int, raw_input().split()))
)

for _ in xrange(input()):
    (command, newSet) = (
        raw_input().split()[0],
        set(map(int, raw_input().split()))
    )

    # Cool trick. Since our commands are method names, just
    # execute the method on A with our new set as its argument.
    getattr(A, command)(newSet)

print str(sum(A))'''