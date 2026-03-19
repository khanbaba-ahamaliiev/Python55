# 1
# Створіть програму, яка відображає меню з опціями для вибору:
# 1 — додавання двох чисел, 2 — віднімання двох чисел, 3 — ділення двох чисел,
# 4 — вихід. Програма має запитувати в користувача номер опції і, якщо обрано
# пункт 1, 2 або 3, запитувати введення двох чисел, після чого виконувати обрану
# операцію: додавати (якщо обрано 1), віднімати (якщо обрано 2) або ділити
# (якщо обрано 3) введені числа. Результат операції має бути виведено на екран.
# У разі вибору пункту 4 програма завершує роботу, виводячи повідомлення про
# вихід. Якщо введено некоректну опцію, програма має повідомити про помилку і
# знову показати меню. Програма має працювати в циклі, повторюючи виведення меню
# і виконання дій доти, доки не буде обрано вихід.

while True:
    print(" menu: ")
    print("1. додавання")
    print("2. віднімання")
    print("3. ділення")
    print("4. завершити обрахування")

    choice = int(input("Enter your choice: "))
    if choice == 1 or choice == 2 or choice == 3:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        if choice == 1:
            print(f"{a} + {b} = {a+b}")
        elif choice == 2:
            print(f"{a} - {b} = {a-b}")
        elif choice == 3:
            if b == 0:
                print("error")
            else:
                print(f"{a} / {b} = {a/b}")
    elif choice == 4:
        print("завершити обрахування")
        break
    else:
        print("invalid choice")

# 2
# Користувач вводить висоту трикутника і символ для заповнення. Програма повинна відобразити рівносторонній трикутник.
# Приклад введення:
# Введіть висоту трикутника: 4.
# Введіть символ: #.
# Приклад виведення:
#    #
#   ###
#  #####
# #######

height = int(input("Enter your height: "))
sym = input("Enter your symbol: ")
i = 1

for i in range(1, height + 1):
    nothing = height - i
    print(" " * nothing + sym * (2 * i - 1))
# 3
# Написати програму, яка перевіряє користувача на знання таблиці множення.
# Програма виводить на екран два числа, користувач має ввести їхній добуток.
# Розробити кілька рівнів складності (відрізняються складністю та кількістю запитань).
# Наприклад, в рівні буде 10 запитань, необхідно порахувати кількість вірних і не вірних відповідей.
# Вивести користувачеві оцінку його знань. якщо відповів 3 з 10 - оцінка не задовільно,
# 5 з 10 - задовільно, 8 з 10 - добре, 10 з 10 - відмінно
import random
print("виберіть складність : ")
print("1. легка")
print("2. середня")
print("3. складна")

choice = int(input("Enter your choice: "))
correct = 0
wrong = 0
if choice == 1:
    for i in range(10):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        dob = n1 * n2
        print(f"{n1} * {n2} =")
        result = int(input("Enter your answer: "))
        if result == dob:
            correct += 1
            print("правильно")
        else:
            wrong += 1
            print("не правильно")
elif choice == 2:
    for i in range(10):
        n1 = random.randint(1, 10)
        n2 = random.randint(11, 100)
        dob = n1 * n2
        print(f"{n1} * {n2} =")
        result = int(input("Enter your answer: "))
        if result == dob:
            correct += 1
            print("правильно")
        else:
            wrong += 1
            print("не правильно")
elif choice == 3:
    for i in range(10):
        n1 = random.randint(1, 10)
        n2 = random.randint(11, 20)
        n3 = random.randint(20, 100)
        dob = n1 * n2 * n3
        print(f"{n1} * {n2} *{n3} =")
        result = int(input("Enter your answer: "))
        if result == dob:
            correct += 1
            print("правильно")
        else:
            wrong += 1
            print("не правильно")
print(f"кількість вірних відповідей: {correct} из 10")
print(f"кількість не правильних відповідей: {wrong} из 10")

if correct <= 3:
    print("оцінка не задовільно")
elif correct <= 5:
    print("задовільно")
elif correct <= 9:
    print("добре")
elif correct == 10:
    print("відмінно")

#Завдання 4 шахова доска

 # ***---***---***---***---
 # ***---***---***---***---
 # ***---***---***---***---
 # ---***---***---***---***
 # ---***---***---***---***
 # ---***---***---***---***


n = int(input("Enter your size: "))
for i in range(1, 5):
    for i in range(1, n+1):
        for j in range(1, 9):
            print("*" * n + "-" * n, end="")
        print()
    for i in range(1, n+1):
        for j in range(1, 9):
            print("-" * n + "*" * n, end="")
        print()
