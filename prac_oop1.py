class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Ім’я: {self.name}, вік: {self.age}")


student1 = Student("John", 25)
student2 = Student("Mark", 21)
student3 = Student("Maria", 23)

students = []
students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    student.show_info()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def show_area(self):
        print(f"S = {3.14*(self.radius)**2}")

circle1 = Circle(5)
circle1.show_area()

circle2 = Circle(7)
circle2.show_area()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount >0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def show_info(self):
        print(f"{self.owner}'s balance is {self.balance}")

user = BankAccount("John", 100)
user.deposit(50)
user.withdraw(20)
user.show_info()


class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        if self.is_ready == False:
            self.is_ready = True
            print(f"{self.brand} {self.year} is ready")

    def move(self):
        if self.is_ready == True:
            print(f"{self.brand} {self.year} is moving")
        else:
            print(f"{self.brand} {self.year} is not ready move")

    def show_info(self):
        print(f"car brand: {self.brand} year: {self.year} ready: {self.is_ready}")

car1 = Car("toyota", 2021)
car1.start_engine()
car1.move()
car1.show_info()

car2 = Car("mersedes", 2017)
car2.move()
car2.show_info()
