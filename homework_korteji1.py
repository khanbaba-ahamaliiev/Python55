import random

# Завдання 1
# Є кортеж з назвами міст. Виведіть ті міста, які
# зустрічаються в кортежі більше одного разу.

cities = (
    "kyiv",
    "lviv",
    "odesa",
    "kharkiv",
    "dnipro",
    "lviv",
    "kyiv",
    "ternopil",
    "odesa",
    "poltava",
    "sumy",
    "dnipro",
)

shown = []

for city in cities:
    if cities.count(city) > 1 and city not in shown:
        print(city)
        shown.append(city)

# Завдання 2
# Є два кортежі з випадковими числами. Виведіть на екран
# ті числа, які є в першому кортежі, але немає в другому.

tup1 = {random.randint(1, 20) for _ in range(10)}
print(tup1)
tup2 = {random.randint(1, 20) for _ in range(10)}
print(tup2)

for num in tup1:
    if num not in tup2:
        print(num, end=" ")

print()

# Завдання 3
# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()


def same_elements(tup1, tup2):
    result = []
    for a, b in zip(tup1, tup2, strict=False):
        if a == b:
            result.append(a)

    return result


t1 = (1, 2, 3, 4, 5)
t2 = (1, 7, 3, 8, 5)

print(same_elements(t1, t2))
