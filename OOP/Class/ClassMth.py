# Class Methods allow operations related to the class itself
#   They take (cls) as the first parameter, which represent the class
#   itself

class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name} has a gpa of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students are {cls.count} students"

student1 = Student("Ronald", 4.50)
print(student1.get_info())

student2 = Student("Dorinano", 3.99)
print(student2.get_info())

student3 = Student("Steve", 3.14)
print(student3.get_info())

student4 = Student("D-boy", 3.53)
print(student4.get_info())

print(Student.get_count())