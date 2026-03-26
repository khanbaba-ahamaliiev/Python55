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


# Додаткове завдання 1

class BankCard:
    def __init__(self, owner, balance, pin, daily_limit, withdrawn_today):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.daily_limit = daily_limit
        self.withdrawn_today = withdrawn_today

    def authorization(self, your_pin):

        if your_pin == str(self.pin):
            print("your pin is valid, welcome")
            return True


        else:
            print("your pin is not valid")
            return False

    def deposit(self, amount):
        if not self.authorization:
            print("authorization failed")
        else:
            print("authorization successful")

        if amount > 0:
            self.balance += amount
        else:
            print("amount cannot be negative")

    def withdraw(self, amount):
        if not self.authorization:
            print("authorization failed")
        else:
            print("authorization successful")

        if amount >= self.daily_limit:
            print("you have daily limit")
        else:
            if self.balance >= amount:
                self.balance -= amount
                self.withdrawn_today += amount

    def reset_daily_limit(self):
        new_day = True
        if new_day:
            self.daily_limit = 0

    def show_info(self):
        print(f"{self.owner}'s balance is {self.balance}, pin: {self.pin}, \ndaily limit: {self.daily_limit}, withdrawn_today: {self.withdrawn_today} ")
user = BankCard("John", 1000, 1234, 500, 0)

user.authorization(1234)
user.deposit(500)
user.withdraw(200)
user.show_info()


class Car:
    def __init__(self, brand, year, fuel, fuel_consumption, mileage, is_engine_on=False):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.mileage = mileage
        self.is_engine_on = is_engine_on

    def start_engine(self):
        if not self.is_engine_on:
            self.is_engine_on = True
            print(f"{self.brand} {self.year} is ready")
        else:
            print(f"{self.brand} {self.year} is already ready")

    def stop_engine(self):
        if self.is_engine_on:
            self.is_engine_on = False
            print(f"{self.brand} {self.year} is stopped")
        else:
            print(f"{self.brand} {self.year} is already stopped")

    def add_fuel(self, litres):
        self.fuel += litres
        print(f"{self.brand} {self.year} is added {litres} litres fuel")

    def moving(self, distance):
        if not self.is_engine_on:
            print(f"{self.brand} {self.year} need to start engine")
        else:
            if distance < (self.fuel/self.fuel_consumption):
                self.mileage += distance
                self.fuel -= distance * self.fuel_consumption
            else:
                print(f"{self.brand} {self.year} not enough fuel")
                print(f"you can move {self.fuel/self.fuel_consumption} km")

    def show_info(self):
        print(f"{self.brand} {self.year}, mileage: {self.mileage}, fuel: {self.fuel}, is_engine_on: {self.is_engine_on}")

car1 = Car("toyota", 2021, 100, 8, 1230)
car1.start_engine()
car1.add_fuel(12)
car1.moving(5)
car1.show_info()
