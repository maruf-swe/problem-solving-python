n = int(input())
if n % 2 == 0:
    if n in range(2, 5) or n > 20:
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
else:
    print("Weird")



print("Optional solution")

if n % 2 == 0:
    if 2 <= n <= 5 or n > 20:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
else:
    print("Weird")

