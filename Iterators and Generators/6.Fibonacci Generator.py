def fibonacci():
    while True:
        a = 0
        b = 1
        yield a
        yield b
        while True:
            next_num = a + b
            yield next_num
            a = b
            b = next_num




generator = fibonacci()
for i in range(5):
    print(next(generator))
