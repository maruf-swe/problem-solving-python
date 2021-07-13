def solve(s):
    l = s.split(" ")
    a = [i.capitalize() for i in l]
    return " ".join(a)

s = input()
print(solve(s))


'''
m = input().split(' ')  didn't work properly. Every letter seperated
n = ''
for i in m:
    n += i.capitalize()
print(' '.join(n))

def solve(s):  #16 point get by submit this. one test case wrong
    solve = s.title()
    return solve
s = input()
print(solve(s))

solution 2
#import string
#print(string.capwords(input(), ' '))

solution 3
string = input().split(' ')
print(' '.join((word.capitalize() for word in string)))'''