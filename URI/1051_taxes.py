salary = float(input())
if (salary >= 0 and salary <= 2000):
    print("Isento")
elif (salary >= 2000.01 and salary <= 3000):
    salary = salary - 2000
    pay_tax = salary * .08
    print("R$ %.2f" % pay_tax)
elif (salary >= 3000.01 and salary <= 4500):
    salary = salary - 3000
    pay_tax = salary * .18 + 80
    print("R$ %.2f" % pay_tax)
else:
    salary = salary - 4500
    pay_tax = salary * .28 + 350
    print("R$ %.2f" % pay_tax)
