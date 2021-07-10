# Access both key and value using items()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)

# Access both key and value without using items()
for key in dt:
    print(key, dt[key])
    
