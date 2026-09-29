class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name, self.address)


class Staff(Person):
    def __init__(self, name, address, subject):
        super().__init__(name, address)
        self.subject = subject

    def display(self):
        print(self.name, self.address, self.subject)


class Student(Person):
    def __init__(self, name, address, grade):
        super().__init__(name, address)
        self.grade = grade

    def display(self):
        print(self.name, self.address, self.grade)


s1 = Staff("Rahul", "Pune", "Python")
s2 = Student("Aman", "Patna", "A")

people = [s1, s2]

for p in people:
    p.display()       # Polymorphism

print(isinstance(s1, Staff))
print(isinstance(s2, Student))
print(issubclass(Staff, Person))
print(issubclass(Student, Person))
