employee_salary = float(input())
new_salary = 0
money_earned = 0
percantage = 0
if (employee_salary >= 0 and employee_salary <= 400):
    new_salary = employee_salary * 0.15
    money_earned = employee_salary + new_salary
    percantage = 15
elif (employee_salary >= 400.01 and employee_salary <= 800.00):
    new_salary = employee_salary * 0.12
    money_earned = employee_salary + new_salary
    percantage = 12
elif (employee_salary >= 800.01 and employee_salary <= 1200.00):
    new_salary = employee_salary * 0.1
    money_earned = employee_salary + new_salary
    percantage = 10
elif (employee_salary >= 1200.01 and employee_salary <= 2000.00):
    new_salary = employee_salary * 0.07
    money_earned = employee_salary + new_salary
    percantage = 7
elif (employee_salary > 2000):
    new_salary = employee_salary * 0.04
    money_earned = employee_salary + new_salary
    percantage = 4
print("Novo salario: %.2f" % money_earned)
print("Reajuste ganho: %.2f" % new_salary)
print("Em percentual: {} {}".format(percantage, "%"))
