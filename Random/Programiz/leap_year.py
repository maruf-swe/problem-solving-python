# Python program to check if year is a leap year or not
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# builtin function solution
import calendar


def is_leap(year):
    return calendar.isleap(year)


print(is_leap(int(input("Enter year: "))))

# another solution,,,, if else base
year = int(input("Enter Year: "))

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a Leap Year")
    else:
        print("Leap Year")

else:
    print("NOT a leap year,")


# another ....... function base
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


year = int(input())
print(is_leap(year))
