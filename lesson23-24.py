# for

ls = []
ls.append("Den")  # - добавляет в список что-то
print(ls)

import random

# for _ in range(10):
#     ls.append(random.randint(1 ,100))
# print(ls)


# [выражение for элемент in итератор <if условие>]

ls1 = [random.randint(1, 100) for _ in range(10)]  # генератор списков
print(ls1)

ls2 = [i for i in ls1 if i % 2 == 0]
print(ls2)

ls3 = ["  Den  ", "", "  ", "Bob", "    Alice"]
ls3 = [
    s.strip().title() for s in ls3 if s.strip()
]  # - тут нельзя переменные называть _
print(ls3)

ls4 = [5, -2, 7, -8, 0, -1, 4]
ls4 = [n if n >= 0 else 0 for n in ls4 if n != 5]
print(ls4)

ls5 = []

for y in range(1, 4):
    temp = []
    for x in range(1, 4):
        temp.append(x * y)
    ls5.append(temp)
print(ls5)

print(len(ls1))  # - возвращает длину списка
print(max(ls1))  # - возвращает максимальный элемент
print(min(ls1))  # - возвращает минимальный элемент
print(sum(ls1))  # - возвращает суму значений
print(sorted(ls1))  # - возвращает отсортированный список от мин до макс

line = "hello"
for i, v in enumerate(line):  # - возвращает кортедж
    print(v, i, end=" ")

ls6 = []
ls6.append("hello")
print(ls6)
print(ls6.count("hello"))
print(ls6.pop())  # - удаляет последний елемент
print(ls6)
ls6.clear()
ls6 = [1, 2, 3, 4, 5]
ls6.insert(0, -10)
print(ls6)
ls6.remove(5)

ls7 = [6, 7, 8, 9, 0]
ls6.extend(ls7)
print(*ls6)  # - * перед списком убирает скобки []

ls8 = [3, 4, 5]
ls9 = ls8
ls8[0] = 5
ls9[1] = 5
print(ls8)
print(ls9)

ls10 = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(ls10)

for inner_list in ls10:
    for item in inner_list:
        print(item, end=" ")
    print()
