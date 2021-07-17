spent_time = int(input("How many Hours: "))
speed = int(input())
total_distance = spent_time * speed
fuel_needed = total_distance / 12
print(f'{fuel_needed:.3f}')

# or
spent_time = int(input("How many Hours: "))
speed = int(input())
print(f'{total_distance / 12:.3f}')
