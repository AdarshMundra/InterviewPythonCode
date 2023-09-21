# Write a program in Python to print the Fibonacci series using iterative method.

n = int(input("enter your series"))
i,a,b,c=0,0,1,0
l=[a,b]
while(i<n):
    c=a+b
    a=b
    b=c
    l.append(c)
    i+=1

print(l)


def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series