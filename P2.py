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

