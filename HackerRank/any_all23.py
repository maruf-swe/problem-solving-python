n = int(input())
lists = input().split(' ')
print(all(int(i) >= 0 for i in lists) and any(i == i[::-1] for i in lists))
