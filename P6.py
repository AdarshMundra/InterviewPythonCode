# Write a program in Python to check whether a number is palindrome or not using iterative method.


def checkpalindrome(n):
    if n<0:
        print("not a palindrome")
    else:
        duplicate = str(n)[::-1]
        print(duplicate)
        if duplicate ==str(n):
            print("P")
        else:
            print("N")

checkpalindrome(int(input()))