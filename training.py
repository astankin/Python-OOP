class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        for pair in self.__dict__.items():
            yield pair


nasko = Person("Atanas", 39)

for x in nasko:
    print(x)
