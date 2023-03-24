from math import factorial
# 1.

print("Hallo, my name is Hal!")
name = input("What is your name?")
print(f"Hello, {name}. I am glad to meet you!")

# 2.
print(sum([x for x in range(1, 11)]))

# 3.
print(factorial(10))
result = 0
for i in range(1, 11):
    result += 1 / i
print(result)

# 4.
print("Please enter two numbers:")
num1 = float(input())
num2 = float(input())
print("The sum is:", num1 + num2)
print("The difference is:", num1-num2)
print("The multiply is:", num1 * num2)
print("The multiply is:", (num1 * num2) / 2)
print("The max number is:", max(num1, num2))
print("The min number is:", min(num1, num2))

# 5.
# Python program to find roots of quadratic equation
import math


# function for finding roots
def equation_roots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


# Driver Program
a = int(input())
b = int(input())
c = int(input())

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equation_roots(a, b, c)

