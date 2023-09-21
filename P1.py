#Write a program to reverse an integer in Python.
element = int(input("elter a integer"))

if element>0:
    sign =1
else:
    sign =-1

final_answer = str(abs(element))[::-1]
print(int(final_answer)*sign)


def reverse_integer(n):
    reversed_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n != 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10

    return reversed_num * sign

# Input integer
num = int(input("Enter an integer: "))

# Reverse the integer
reversed_num = reverse_integer(num)

print("Reversed integer:", reversed_num)




