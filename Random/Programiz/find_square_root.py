while True:
    number = int(input("Enter a number: "))
    try:
        if number < 0:
            print("Sorry, input must be a positive integer, try again")
            continue
        break
    except ValueError:
        print("That's not an int!")

square_root = number ** 0.5

print(square_root)