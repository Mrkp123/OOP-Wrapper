print("---- Python OOP Project: Employee Management System -----")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self): 
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary:.1f}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary:.1f}")
        print(f"Department: {self.department}")


def main():
    person = Person("Aryan Patel", 22)
    employee = Employee("Aryan Patel", 22, "E412", 90000.0)
    manager = Manager("Aryan Patel", 22, "E412", 90000.0, "HR")

    print("Choose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")

    choice = input("Enter your choice: ")

    if choice == "1":
        person.display()
    elif choice == "2":
        employee.display()
    elif choice == "3":
        manager.display()
    else:
        print("Invalid choice!")


main()