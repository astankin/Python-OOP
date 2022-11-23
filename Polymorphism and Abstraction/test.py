class Student:
    def __init__(self, size):
        self.stu = [None] * size

    def __setitem__(self, rollno, name):
        # explicitly defined __setitem__
        print("Setting name to rollno", rollno)
        self.stu[rollno] = name

    def __getitem__(self, rollno):
        # explicitly defined __getitem__
        print("Getting name associated with rollno", rollno)
        return self.stu[rollno]


s1 = Student(4)
s1[0] = 'Meghana'
s1[1] = 'Raju'
s1[2] = 'Hari'
s1[3] = 'Sreeja'
print(s1[0])
print(s1[0:4])