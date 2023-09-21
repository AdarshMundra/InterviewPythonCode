#Write a program in Python to find greatest among three integers.

a,b,c=0,10,2

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

print(max(a,b,c))