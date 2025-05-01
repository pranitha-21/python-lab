class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            combined_name = f"{self.name} & {other.name}"
            combined_salary = self.salary + other.salary
            return Employee(combined_name, combined_salary)
        raise TypeError("Unsupported operation between Employee and non-Employee object")

    def __sub__(self, other):
        if isinstance(other, Employee):
            return abs(self.salary - other.salary)
        raise TypeError("Unsupported operation between Employee and non-Employee object")

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"
    
name1 = input("Enter the first employee's name: ")
salary1 = float(input("Enter the first employee's salary: "))

name2 = input("Enter the second employee's name: ")
salary2 = float(input("Enter the second employee's salary: "))

emp1 = Employee(name1, salary1)
emp2 = Employee(name2, salary2)

# Combining employees' salaries
combined_employee = emp1 + emp2
print("Combined Employee:", combined_employee)

# Comparing salaries
salary_difference = emp1 - emp2
print(f"Salary difference between {emp1.name} and {emp2.name}: {salary_difference}")