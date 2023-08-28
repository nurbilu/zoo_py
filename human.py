import sys

def Skip_lines():
    lines_to_skip = 3
    sys.stdout.write(f'\033[{lines_to_skip}A')

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Human):
    def __init__(self, name, age, student_id, field_of_study):
        super().__init__(name, age)
        self.student_id = student_id
        self.field_of_study = field_of_study

    def __str__(self):
        return f"Student ID: {self.student_id}, Field of Study: {self.field_of_study}, {super().__str__()}"



class Worker(Human):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Employee ID: {self.employee_id}, {super().__str__()}"


class Manager(Worker):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def __str__(self):
        return f"Manager, Department: {self.department}, {super().__str__()}"


class Simple(Worker):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def __str__(self):
        return f"Simple Worker, Department: {self.department}, {super().__str__()}"



if __name__ == '__main__':
    # Skip_lines()
    # You can create instances and print them to see the output
   objects= [ 
    Student("Alice", 20, "S12345" , "Econimics"),
    Manager("Charlie", 40, "M24680", "HR"),
    Simple("David", 25, "SW54321", "Operations")
    ]
for obj in objects:
        if isinstance(obj, Student):
            print("This is a Student:")
        elif isinstance(obj, Worker):
            print("This is a Worker:")
        elif isinstance(obj, Manager):
            print("This is a Manager:")
        elif isinstance(obj, Simple):
            print("This is a Simple Worker:")

        print(obj)
        print()
