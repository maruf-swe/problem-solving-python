n = int(input())
C = 0
R = 0
S = 0
for i in range(n):
    amount, ch = list(map(str, input().split()))
    amount = int(amount)
    if (ch == 'C'):
        C += amount
    elif (ch == 'R'):
        R += amount
    else:
        S += amount

total = C + R + S
x = (C * 100.00) / total
y = (R * 100.00) / total
z = (S * 100.00) / total
print(f"Total: {total} cobaias")
print("Total de coelhos:", C)
print("Total de ratos:", R)
print("Total de sapos:", S)
print(f"Percentual de coelhos: {x:.2f} %")
print(f"Percentual de ratos: {y:.2f} %")
print(f"Percentual de sapos: {z:.2f} %")
