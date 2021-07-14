'''
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive
number that is evenly divisible by all of the numbers from 1 to 20?
'''


def is_divisible(n):
    for i in range(11, 21):
        if n % i == 0:
            continue
        else:
            return False
    return True


smallest_number = 2520
while not is_divisible(smallest_number):
    smallest_number += 2520

print(smallest_number)
