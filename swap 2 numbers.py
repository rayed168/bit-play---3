def swap1(a, b):
    print(f"Before swapping : a = {a} and b = {b}")

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(f"After swapping : a = {a} and b = {b}")

def swap2(a, b):
    print(f"Before swapping : a = {a} and b = {b}")

    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1

    print(f"After swapping : a = {a} and b = {b}")
num1 = int(input("Enter the first number : "))

num2 = int(input("Enter the second number : "))

swap1(num1, num2)

swap2(num1, num2)