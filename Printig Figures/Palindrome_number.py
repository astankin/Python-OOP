n = int(input("Enter number:"))
num_to_sting = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if num_to_sting == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

# Using string

num = int(input("Enter number:"))
num_to_sting = str(num)
if num_to_sting == num_to_sting[::-1]:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")