a = int(input())
b = int(input())
print("%0.3f" % ((a * b) / 12))

# for f string time error
spent_time = int(input("How many Hours: "))
speed = int(input())
total_distance = spent_time * speed
fuel_needed = total_distance / 12
print(f'{fuel_needed:.3f}')

# or
spent_time = int(input("How many Hours: "))
speed = int(input())
print(f'{total_distance / 12:.3f}')