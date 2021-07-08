# Program to print half pyramid using *
rows = int(input("How many rows do you want: "))

for i in range(rows):
    for j in range(i + 1):
        print('*', end=" ")
    print()

# Program to print half pyramid using numbers
rows = int(input("How many rows do you want: "))

for i in range(rows):
    for j in range(1, i + 2):
        print(j, end=" ")
    print()

# Program to print half pyramid using alphabates
rows = int(input("How many rows do you want: "))

asci_value = 65
for i in range(rows):
    for j in range(1, i + 2):
        alphate = chr(asci_value)
        print(alphate, end=" ")

    asci_value += 1
    print()

#  Inverted half pyramid using *
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print("\n")

#  Inverted half pyramid using numbers
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\n")
