person_age = int(input())
a = person_age // 365
left_total_days = person_age % 365
total_months = left_total_days // 30
days = left_total_days % 30

print("{} ano(s)".format(a))
print("{} mes(es)".format(total_months))
print("{} dia(s)".format(days))
