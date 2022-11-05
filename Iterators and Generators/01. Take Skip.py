class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        current_num = self.step * self.iterations
        self.iterations += 1
        return current_num

numbers = take_skip(2, 6)
for number in numbers:
    print(number)



