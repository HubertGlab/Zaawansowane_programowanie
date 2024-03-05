class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks)/len(self.marks) > 50


s1 = Student("Madzia", [30, 60, 80, 90])

print(s1.is_passed())
