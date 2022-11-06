def number_increment(numbers):
    def increase():
        result = list(map(lambda x: x + 1, numbers))
        return result

    return increase()


print(number_increment([1, 2, 3]))
