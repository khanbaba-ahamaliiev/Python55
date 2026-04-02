# Завдання 1
import math


class Rectangle:
    def __init__(self, width, height):
        self._width:int = width
        self._height:int = height

    def perimeter(self)->int:
        return 2 * (self._width + self._height)

    def display_info(self):
        print(f"width is {self._width}, height is {self._height}")
        print(f"perimeter is {self.perimeter()}")


class Circle:
    def __init__(self, radius):
        self._radius:float = radius

    def perimeter(self)->float:
        return 2 * math.pi * self._radius

    def display_info(self):
        print(f"radius is {self._radius}")
        print(f"perimeter is {self.perimeter()}")


class Triangle:
    def __init__(self, a, b, c):
        self._a:int = a
        self._b:int = b
        self._c:int = c

    def perimeter(self)->float:
        return self._b + self._a + self._c

    def display_info(self):
        print(f"side a is {self._a}, side b is {self._b}, side c is {self._c}")
        print(f"perimeter is {self.perimeter()}")


def create_figure()->Rectangle | Circle | Triangle | None:
    figure = input("select a figure: ")

    if figure == "Rectangle":
        width = int(input("enter the width: "))
        height = int(input("enter the height: "))
        return Rectangle(width, height)

    elif figure == "Circle":
        radius = float(input("enter the radius: "))
        return Circle(radius)

    elif figure == "Triangle":
        a = float(input("enter the first side: "))
        b = float(input("enter the second side: "))
        c = float(input("enter the third side: "))
        return Triangle(a, b, c)
    else:
        print("invalid input")
        return None


figures = []
for _ in range(3):
    figures.append(create_figure())

for figure in figures:
    if figure is None:
        print("figure is not in mood")
        continue

    figure.perimeter()
    figure.display_info()


# Завдання 2

class Manager:
    def __init__(self, name:str, base_salary:float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary


class Developer:
    def __init__(self, name:str, base_salary:float, work_experience:int):
        self._name = name
        self._base_salary = base_salary
        self.work_experience = work_experience

    def get_salary(self):
        if self.work_experience > 4:
            return self._base_salary * 1.2
        else:
            return self._base_salary


class Inter:
    def __init__(self, name:str, base_salary:float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self):
        return self._base_salary / 2


def create_worker()->Manager | Developer | Inter | None:
    worker_name = input("enter the worker's name: ")

    if worker_name == "Manager":
        name = input("enter the worker's name: ")
        salary = float(input("enter the salary: "))
        return Manager(name, salary)
    elif worker_name == "Developer":
        name = input("enter the worker's name: ")
        salary = float(input("enter the salary: "))
        work_exp = int(input("enter the work experience: "))
        return Developer(name, salary, work_exp)
    elif worker_name == "Inter":
        name = input("enter the worker's name: ")
        salary = float(input("enter the salary: "))
        return Inter(name, salary)
    else:
        print("invalid input")
        return None


workers = []
for _ in range(3):
    worker = create_worker()

for worker in workers:
    if worker is None:
        print("worker is not in mood")
        continue

    print(worker.get_salary())
