def store_results(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        with open('results.txt', 'a') as file:
            file.write(f"Function {func_ref.__name__} was add called. Result: {func_result}\n")
    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
