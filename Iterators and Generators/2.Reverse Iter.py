class reverse_iter:
    def __init__(self, seq):
        self.seq = seq
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value_to_return = self.seq[self.i]
            self.i -= 1
            return value_to_return
        except IndexError:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

