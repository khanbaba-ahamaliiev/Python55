# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (6, 7, 3, 4, 5)

res = []
for i in tuple1:
    if i in tuple2 and i in tuple3:
        res.append(i)
    else:
        continue

print(res)


# Завдання 2
# Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 8)
tuple3 = (6, 7, 3, 4, 5)

res = []
for i in tuple1:
    if i in tuple2 or i in tuple3:
        continue
    else:
        res.append(i)

for i in tuple2:
    if i in tuple1 or i in tuple3:
        continue
    else:
        res.append(i)

for i in tuple3:
    if i in tuple2 or i in tuple1:
        continue
    else:
        res.append(i)

print(res)
# Завдання 3
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в
# кожному з них на тій самій позиції.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 2, 5, 6, 5)
tuple3 = (3, 2, 4, 6, 5)

res = []
for i in range(len(tuple1)):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        res.append(tuple1[i])
    else:
        continue

print(res)
