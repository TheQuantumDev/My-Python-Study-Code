# Static methods are best for utility functions that do not need
# access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["CEO", "Manager", "Senior Dev", "Junior Dev"]
        return position in valid_positions
    
employee1 = Employee("Ronald", "CEO")
print(employee1.get_info())

employee2 = Employee("Dorinano", "Manager")
print(employee2.get_info())

employee3 = Employee("Steve", "Senior Dev")
print(employee3.get_info())

employee4 = Employee("D-boy", "Junior Dev")
print(employee4.get_info())

print(Employee.is_valid_position("CEO"))