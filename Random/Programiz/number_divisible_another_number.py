num_list = list(map(int, input("Enter the Numbers by Space Separated: ").split()))
n = int(input("Enter the divisible number: "))
result = list(filter(lambda x: x % n == 0, num_list))
print("The numbers divisible by", n, "are", result)
