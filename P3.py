#Write a program in Python to check given number is prime or not.

def checkPrime(n):
    i,temp=0,True
    for i in range(2,n//2):
        if n%i == 0:
            temp=False
            break
    return temp


n = int(input("enter your number =>"))
print(checkPrime(n))

# def is_prime(number):
#     if number <= 1:
#         return False  # 0 and 1 are not prime numbers

#     if number <= 3:
#         return True  # 2 and 3 are prime numbers

#     if number % 2 == 0 or number % 3 == 0:
#         return False  # Numbers divisible by 2 or 3 are not prime

#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6

#     return True

# # Input integer
# num = int(input("Enter an integer: "))

# # Check if it's a prime number
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")
