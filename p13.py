#Write a program in Python to add two integer without using arithmetic operator?
def add_without_arithmetic_operator(a, b):
    while b != 0:
        carry = a & b  # Calculate the carry using bitwise AND
        a = a ^ b      # Calculate the sum using bitwise XOR
        b = carry << 1  # Shift the carry to the left by 1 position

    return a

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Add the integers without using arithmetic operators
sum_result = add_without_arithmetic_operator(num1, num2)

print("Sum of", num1, "and", num2, "is:", sum_result)
