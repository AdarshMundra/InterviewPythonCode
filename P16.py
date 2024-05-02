# Python program to print first n Prime Number with explanation.

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_n_primes(n):
    """Print the first n prime numbers."""
    if n <= 0:
        return

    prime_count = 0
    num = 2  # Start with the first prime number

    while prime_count < n:
        if is_prime(num):
            print(num, end=" ")
            prime_count += 1
        num += 1

# Input the number of prime numbers to print
n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("The first", n, "prime numbers are:")
    print_n_primes(n)

