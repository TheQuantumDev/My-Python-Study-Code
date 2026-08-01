# Class variables are defined outside of the constructor, they shared amongst objects of a class

class Student:
    work = "Programmer" # Class Variable
    num_of_students = 0 # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("Reodesu", 14)
student2 = Student("Dorinano", 13)
student3 = Student("Emmanuel", 15)

print(f"The name of the first student is {student1.name}, he is {student1.age} years old.")

print(f"The name of the second student is {student2.name}, he is {student2.age} years old.")

print(f"The name of the third student is {student3.name}, he is {student3.age} years old.")

print(f"They are all {Student.work}")

print(f"There are {Student.num_of_students} students")