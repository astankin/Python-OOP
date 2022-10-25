class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "["+', '.join(reversed(self.data))+"]"


stak = Stack()
stak.push("a")
stak.push("b")
stak.push("c")
stak.push("d")
stak.push("e")

print(stak)