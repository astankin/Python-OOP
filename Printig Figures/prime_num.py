def check_is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not a prime number"
        return f"{num} is a prime number"
    return f"{num} is not a prime number"


number = int(input())
print(check_is_prime(number))