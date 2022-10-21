class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality




person = Person("Atanas", 39, "Bulgarian")
person_dict = person.__dict__
print(person_dict)
