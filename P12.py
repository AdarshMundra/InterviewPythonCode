# Write a program in Python to find prime factors of a given integer.
def prime_factors(n):
    factors = []
    divisor = 2  # Start with the smallest prime number

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        print(divisor)
    return factors

# Input an integer
num = int(input("Enter an integer: "))

if num <= 1:
    print("Prime factors are not defined for numbers less than or equal to 1.")
else:
    # Find and print the prime factors
    factors = prime_factors(num)
    print("Prime factors of", num, "are:", factors)
