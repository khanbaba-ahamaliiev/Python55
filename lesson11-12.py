# isinstance - определяет относится ли значение к типу или нет
x = 5
print(isinstance(x, int))
print(isinstance(x, float))

# match - новый оператор, подбирает 1 подходящий кейс

# match <variables>:
# ....case <variables_value1>
# .........code

x = 6

match x:
    case 1:
        print("1")
    case 2 | 3 | 4:
        print("мале число: 2-4")
    case 5 | 6 | 7:
        print("середнє число: 5-7")
    case 8:
        print("8")
    case _:  # - все остальные значения
        print("other")

x = None
x = str(x)

match x:
    case "True":
        print("True")
    case "False":
        print("False")
    case "None":
        print("None")
    case _:
        print("other")

x = 10

match x:
    case 1:
        print("1")
    case value:
        print("other", value)

# guard
years = int(input("Enter a number: "))
match years:
    case y if y < 1:
        print("no award")
    case y if 1 <= y < 3:
        print("award 5%")
    case y if 3 <= y < 5:
        print("award 10%")
    case y if y > 5:
        print("no award 15%")


import math

# D = b*b / 4 * a * c
print("x^2-bx+c=0")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

# D > 0 - 2 решения
# D = 0 - 1 решение
# D < 0 - нету решений

D = (b**2) - 4 * a * c


if D > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print(f"2 корені x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"1 корен x = {x}")
elif D < 0:
    print("немає коренів")
else:
    print("помилка")


salary = float(input("Enter your salary: "))
work_year = float(input("Enter your work year: "))

if work_year < 1:
    print("no award")
elif work_year < 3:
    bonus = salary * 0.05
    print(f"award: {bonus}")
elif work_year < 5:
    bonus = salary * 0.1
    print(f"award: {bonus}")
else:
    bonus = salary * 0.15
    print(f"award: {bonus}")
