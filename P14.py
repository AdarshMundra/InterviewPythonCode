def is_perfect_number(num):
    if num <= 0:
        return False

    divisor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num

# Input an integer
num = int(input("Enter an integer: "))

if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
