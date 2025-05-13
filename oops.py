class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, salary=0):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Salary: ₹{self.salary}")

p1 = Person("Alice")
e1 = Employee("Bob", 30, "EMP123", 50000)
e2 = Employee("Charlie", 25, "EMP124")

print("== Person ==")
p1.display_info()

print("\n== Employee 1 ==")
e1.display_info()

print("\n== Employee 2 ==")
e2.display_info()
