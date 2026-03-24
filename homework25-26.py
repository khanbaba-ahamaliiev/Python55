# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст,
# зазначений нижче:
# "Don't compare yourself with anyone in this world…
#     if you do so, you are insulting yourself."
#         Bill Gates


def text():
    print(
        '"Don\'t compare yourself with anyone in this world… \n\tif you do so, you are insulting yourself."\n\t\tBill Gates'
    )


text()


# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні
# числа між ними.
def range_of_numbers(n1, n2):
    for n in range(n1 + 1, n2):
        if n % 2 == 0:
            print(n, end=", ")
    print()


n1 = 10
n2 = 20

range_of_numbers(n1, n2)


# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого
# символу. Функція приймає як параметри: довжину сторони квадрата, символ і
# змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.
def square(length, symbol, type):
    if type == True:
        for i in range(length):
            for j in range(length):
                print(symbol, end="  ")
            print()
    else:
        for i in range(length):
            for j in range(length):
                if i == 0 or i == length - 1 or j == 0 or j == length - 1:
                    print(symbol, end="  ")
                else:
                    print(" ", end="  ")
            print()


square(6, "*", False)

# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел.
# Числа передаються як параметри))


def find_min(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)


print(find_min(10, 20, 33, 4, 5))

# Завдання 5
# Напишіть функцію, яка рахує кількість цифр у числі. Число передається
# як параметр. З функції потрібно повернути отриману кількість цифр.
# Наприклад, якщо передали 3456, кількість цифр буде 4.


def amount_of_numbers(number):
    return len(str(number))


number = int(input("Enter a number: "))
print(amount_of_numbers(number))

# Завдання 6
# Напишіть функцію, яка перевіряє чи є число паліндромом. Число
# передається як параметр. Якщо число паліндром, потрібно повернути з функції
# true, інакше false.
# "Паліндром" — це число, у якого перша частина цифр дорівнює другій
# перевернутій частині цифр. Наприклад, 123321 — паліндром
# (перша частина 123, друга 321, яка після перевороту стає 123), 546645 —
# паліндром, а 421987 — не паліндром.


def padindrom(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


print(padindrom(30103))
