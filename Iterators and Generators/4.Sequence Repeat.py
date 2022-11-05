class sequence_repeat:
    def __init__(self, seq, n):
        self.seq = seq
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.n:
            raise StopIteration
        symbol = self.i % len(self.seq)
        self.i += 1
        return self.seq[symbol]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
