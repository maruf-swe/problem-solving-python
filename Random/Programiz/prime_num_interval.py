lower_value = int(input())
upper_value = int(input())


for num in range(lower_value, upper_value+1):
    if num> 1:
        for i in range(2, num):
            if num % i ==0:
                break
        else:
            print(num)

