# Python Program to calculate factorial using iterative method.

number = int(input("Enter number the factorial => "))
mul =1
for i in range(1,number+1):
    mul = mul*i

print(mul)


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else :
        return (n * factorial(n-1))

print(factorial(number))