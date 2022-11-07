def even_parameters(function):
    def wrapper(*nums):
        for elem in nums:
            if not isinstance(elem, int) or elem % 2 == 1:
                return "Please use only even numbers!"
        return function(*nums)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))



