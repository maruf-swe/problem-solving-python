def is_panidrome(i):
    return str(i) == str(i)[::-1]


max_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        if is_panidrome(p) and p > max_palindrome:
            max_palindrome = p

print(max_palindrome)
