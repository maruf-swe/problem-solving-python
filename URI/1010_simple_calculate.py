x = input().split()
y = input().split()
p_code1, unit1, price1 = x
p_code2, unit2, price2 = y
sum_total = int(unit1) * float(price1) + int(unit2) * float(price2)
print("VALOR A PAGAR: R$ %0.2f" % sum_total)  # print(f'VALOR A PAGAR: R$ {sum:.2f}')----> occurs runtime error
