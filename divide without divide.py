def divide(our_dividend, our_divisor):
    sign = (-1 if ((our_dividend < 0) ^ (our_divisor < 0))else 1)
    our_dividend = abs(our_dividend)
    our_divisor = abs(our_divisor)

    quotient_number = 0
    temp_number = 0
    for i in range(31, -1, -1):
        if (temp_number + (our_divisor << i) <= our_dividend):
            temp_number += our_divisor << i
            quotient_number |= 1 << i
    if sign == -1:
        quotient_number -= quotient_number
    return quotient_number

a = int(input("Enter a for a/b : "))

b = int(input("Enter b for a/b : "))

print(f"Result of {a} / {b} is {divide(a, b)} ")