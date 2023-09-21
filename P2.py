#Write a program in Python to check whether an integer is Armstrong number or not.

element=int(input("Enter the number"))

duplicate = element
sum1 =0
while(duplicate>0):
    last_digit = duplicate %10
    sum1 =sum1+last_digit**3
    duplicate = duplicate//10
print(sum1)
if sum1== element:
    print("done")
else:
    print("NORT")


def is_armstrong_number(n):
    # Convert the integer to a string to count its digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate the sum of its digits, each raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if it's equal to the original number
    return armstrong_sum == n

# Input integer
num = int(input("Enter an integer: "))

# Check if it's an Armstrong number
if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


