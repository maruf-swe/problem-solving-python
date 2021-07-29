count_even = 0
count_odd = 0
count_positive = 0
count_neg = 0
for i in range(5):
    values = float(input())
    if values % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    if values > 0:
        count_positive += 1
    elif values < 0:
        count_neg += 1

print(count_even, "valor(es) par(es)")
print(count_odd, "valor(es) impar(es)")
print(count_positive, "valor(es) positivo(s)")
print(count_neg, "valor(es) negativo(s)")
