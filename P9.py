# Write a program in Python to check if a number is binary?
    
def is_binary(number):
    # Convert the number to a string for easy character checking
    num_str = str(number)
    
    # Check if each character in the string is '0' or '1'
    for digit in num_str:
        if digit not in ('0', '1'):
            return False
    
    return True

# Input the number to check
num = input("Enter a number: ")

if is_binary(num):
    print(num, "is a binary number.")
else:
    print(num, "is not a binary number.")
