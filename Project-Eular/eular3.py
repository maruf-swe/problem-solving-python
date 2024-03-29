'''
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


def largest_prime_factor(n):
    i = 2
    while i < n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
