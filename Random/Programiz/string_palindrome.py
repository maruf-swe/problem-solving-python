# Program to check if a string is palindrome or not

# with built in function
my_str = input()
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list[my_str] == list[rev_str]:
    print(my_str, "is a palindrome")
else:
    print(my_str, "is not a palindrome")


# solution by function

def is_palindrome(s):
    return s[::-1]


txt = input("Enter a string: ")
ans = is_palindrome(txt)
if ans:
    print(txt, "is palindrome")
else:
    print(txt, "is palindrome")


# another solution


def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


s = input("Enter a string: ")
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

# another solution

st = 'malayalam'
j = -1
flag = 0
for i in st:
    if i != st[j]:
        j = j - 1
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")
