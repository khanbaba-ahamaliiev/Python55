# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно
# порахувати, скільки у списку парних і непарних чисел. Результати вивести на екран.
ls = list(int(i) for i in input("Enter a list: ").split())
even = 0
odd = 0
for i in ls:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"кількість парний: {even} \nкількість не парних: {odd}")

# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно
# визначити максимальне і мінімальне значення у списку. Результати вивести на екран.
ls = list(int(i) for i in input("Enter a list: ").split())
print(f"максимальне значення в списку: {max(ls)} \nмінімальне значення в списку: {min(ls)}")

# Завдання 3
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний
# # елемент і максимальний, від'ємний елемент, порахувати кількість від'ємних елементів, порахувати
# кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран.

import random
ls = list(random.randint(-20,20) for _ in range(10))
print(ls)

ls_poz = list(i for i in ls if i > 0)
ls_neg = list(i for i in ls if i < 0)

nul = 0
for i in ls:
    if i % 10 == 0:
        nul += 1

print(f"мінімальний, додатний елемент: {min(ls_poz)} \nмаксимальний, від'ємний елемент: {max(ls_neg)} \nкількість від'ємних елементів: {len(ls_neg)} \nкількість додатних елементів: {len(ls_poz)} \nкількість нулів: {nul}")
# Завдання 4
# Користувач із клавіатури вводить список цілих чисел і деяке число. Необхідно видалити зі
# списку всі елементи, які менші за задане число. Результат вивести на екран.
ls = list(int(i) for i in input("Enter a list: ").split())
number = int(input("Enter a number: "))

new_ls = list(i for i in ls if i >= number)
print(new_ls)


# Завдання 5
# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12.
# Необхідно вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз
# може складатися тільки з трьох частин: число, операція, число. Можливі операції: +, -, *, /.
question = input("Enter a question: ")

ls = []
number = ""

for i in question:
    if i.isdigit():
        number += i
    else:
        ls.append(int(number))
        ls.append(i)
        number = ""
ls.append(int(number))

print(ls)

if ls[1] == "+":
    print(f"result: {ls[0]} + {ls[2]} = {ls[0] + ls[2]}")
elif ls[1] == "-":
    print(f"result: {ls[0]} - {ls[2]} = {ls[0] - ls[2]}")
elif ls[1] == "*":
    print(f"result: {ls[0]} * {ls[2]} = {ls[0] * ls[2]}")
elif ls[1] == "/":
    print(f"result: {ls[0]} / {ls[2]} = {ls[0] / ls[2]}")
else:
    print("error")

# Завдання 6
# Користувач із клавіатури вводить список цілих чисел. Необхідно відсортувати цей список так,
# щоб від'ємні числа залишилися на своїх місцях, а решта елементів були відсортовані за зростанням.'
# ' Результат вивести на екран.)
ls = list(int(i) for i in input("Enter a list: ").split())

sort_poz_ls = sorted(list(i for i in ls if i >= 0))
print(sort_poz_ls)

result = []
i = 0
for _ in ls:
    if _ < 0:
        result.append(_)
    else:
        result.append(sort_poz_ls[i])
        i += 1

print(result)
