# Завдання 1
# Користувач вводить висоту трикутника і символ для заповнення. Програма
# повинна вивести трикутник, вирівняний по правому краю.
h = int(input("Enter a height: "))
s = input("Enter a symbol: ")

for _ in range(1,h+1):
    formula = s * _
    print(formula)

# Завдання 2
# Користувач вводить розміри дошки (ширину і висоту) і два символи для клітинок.
# Програма повинна відобразити шахову дошку, використовуючи ці символи.

h = int(input("Enter a height: "))
w = int(input("Enter a width: "))

s1 = input("Enter a symbol: ")
s2 = input("Enter a symbol: ")

for i in range(h):
    for j in range(w):
        if (i + j) % 2 == 0:
            print(s1, end="")
        else:
            print(s2, end="")
    print()

# Завдання 3
# Програма випадковим чином загадує чотиризначне число без цифр, що повторюються.
# Користувач повинен спробувати вгадати це число, вводячи свої варіанти. Після
# кожного введення програма повідомляє:
# Кількість цифр, які стоять на своїх місцях (бики).
# Кількість цифр, які є в числі, але стоять не на своїх місцях (корови).

import random

while True:
    n1 = random.randint(1, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)

    if n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4:
        break
number = n1 * 1000 + n2 * 100 + n3 * 10 + n4
secret_number = str(number)

print(secret_number) #- якщо потрібно перевірити що за число загадане

while True:

    answer = input("Enter a number: ")
    bulls = 0
    cows = 0

    if len(answer) != 4:
        print("Помилка! Введи чотиризначне число.")
        continue

    for i in range(4):
        if answer[i] == secret_number[i]:
            bulls += 1

    for i in range(4):
        for j in range(4):
            if i != j and answer[i] == secret_number[j]:
                cows += 1

    print(f"Бики: {bulls}, Корови: {cows}")

    if bulls == 4:
        print(f"Вітаю! Ти вгадав число: {secret_number}")
        break

# Завдання 4
# Число Армстронга — це число, яке дорівнює сумі своїх цифр, піднесених до степеня,
# що дорівнює кількості цифр.
# Напишіть програму, яка:
# Приймає одне число від користувача.
# Перевіряє, чи є воно числом Армстронга.
# Виводить відповідний результат.

number = input("Enter a number: ")

amt_number = len(number)
armstrong = 0
for i in number:
    armstrong += int(i) ** amt_number

if int(number) == armstrong:
    print(f"{number} це число Армстронга")
else:
    print(f"{number} це не є число Армстронга")
# Завдання 5
# Користувач вводить висоту ромба (непарне число) і символ для заповнення.
# Програма повинна вивести заповнений ромб.

h = int(input("Enter a height: "))
s = input("Enter a symbol: ")
mid = h // 2

for _ in range(h):
    if _ <= mid:
        symbols = _ + 1
    else:
        symbols = h - _

    print(s * symbols)

# Завдання 6
# Користувач вводить висоту ромба (непарне число) і символ для заповнення.
# Програма повинна вивести порожнистий ромб.
# Приклад введення:
# Введіть висоту: 7.
# Введіть символ: #.

h = int(input("Enter a height: "))
s = input("Enter a symbol: ")

mid = h // 2

for i in range(h):
    if i <= mid:
        nothing = mid - i
        if i == 0:
            print(" " * nothing + s)
        else:
            print(" " * nothing + s + " " * (2 * i - 1) + s)
    else:
        nothing = i - mid
        formula = h - i - 1
        if formula == 0:
            print(" " * nothing + s)
        else:
            print(" " * nothing + s + " " * (2 * formula - 1) + s)


