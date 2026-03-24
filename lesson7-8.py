# Занятие 7-8
# МОДУЛЬ - папка с файлами

import random  # - импорт файла целиком

print(random.randint(-5, 10))

from random import randint  # - импорт определенной функции

print(randint(-5, 10))

from random import randint as ri  # - импорт и переименование функции

print(ri(1, 10))

# random берет за основу(зерно) время на компьютере

x = random.randint(-5, 10)  # - берет случайное число
print(x)
x = random.randrange(0, 20, 5)  # - берет случайное число в диапазоне с шагом
print(x)
x = random.random()  # - дает случайное число от 0 до 1
print(x)
l = [1, 2, 3, 4, 5]
random.shuffle(l)  # - перемешивает коллекцию
print(l)
x = random.choice("Hello")  # - берет случайное значение
print(x)

# math, datetime
import math

print(math.ceil(5.45))  # - округляет в большую сторону
print(math.floor(5.45))  # - округляет в меньшую сторону
print(math.pow(2, 4))  # - в степень
print(math.sqrt(25))  # - корень

from datetime import date, datetime, time

my_date = date(2020, 5, 12)
print(my_date.strftime("%A %d %B %Y"))

today = date.today()
print(today.strftime("%A %d %B %Y"))

current_time = time(20, 25, 10)
print(current_time)

x = datetime(2020, 5, 12, 20, 10, 5)
print(x.strftime("%A %d %B %Y %H:%M:%S"))

print(datetime.now())

import time

start = time.perf_counter()  # чтобы время считало

time.sleep(5)

end = time.perf_counter()
print(end - start)
