i = 1
j = 7
while True:
    print(f'I={i} J={j}')
    j -= 1
    if j == 4:
        i += 2
        j = 7
    if i == 11:
        break
# another solution
for i in range(1, 10, 2):
    for j in range(7, 4, -1):
        print(f"I={i} J={j}")
