class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary, courses):
        super().__init__(name, age)
        self.salary = salary
        self.courses = courses


class Student(SchoolMember):
    def __init__(self, name, age, courses):
        super().__init__(name, age)
        self.courses = courses
