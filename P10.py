# Write a program in Python to find sum of digits of a number using recursion?

def sumofdigit(num):
    num =str(num)
    sum =0
    for i in num:
        sum = sum+int(i)
    
    print(sum)

sumofdigit(1342)
def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    else:
        # Get the last digit of the number
        last_digit = number % 10
        
        # Recursively compute the sum of digits for the remaining part of the number
        remaining_sum = sum_of_digits_recursive(number // 10)
        
        # Return the sum of the last digit and the sum of digits for the remaining part
        return last_digit + remaining_sum

# Input an integer
num = int(input("Enter an integer: "))

# Calculate and print the sum of its digits using recursion
sum_of_digits = sum_of_digits_recursive(abs(num))
print("Sum of digits:", sum_of_digits)
