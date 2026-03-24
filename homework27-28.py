# Завдання 2
# Напишіть рекурсивну функцію, яка обчислює суму цифр заданого числа.
# Приклад:
# • Введення: 123
# • Виведення: 6 (оскільки 1+2+3=6).


def summa(n):
    if n == 0:
        return 0
    return n % 10 + summa(n // 10)


number = int(input("Enter a number: "))

print(summa(number))

# Завдання 3
# Напишіть рекурсивну функцію, яка перевіряє, чи є заданий список симетричним.
# Симетричний список — - це список, у якому елементи зліва направо і справа наліво збігаються.
# Приклад:
# Введення: [1,2,3,2,1]
# • Висновок: "Список симетричний".


def simetrical(ls):
    if len(ls) <= 1:
        return True

    if ls[0] != ls[-1]:
        return False

    return simetrical(ls[1:-1])


ls = list(int(i) for i in input("Enter a list: ").split())

if simetrical(ls):
    print("Список симетричний")
else:
    print("Список не симетричний")

# Завдання 4
# Написати гру "Бики та корови". Програма "загадує" чотирицифрове число і гравець має вгадати його.
# Після введення користувачем числа програма повідомляє, скільки цифр числа вгадано (бики) і скільки
# цифр вгадано і стоїть на потрібному місці (корови). Після відгадування числа на екран необхідно
# вивести кількість зроблених користувачем спроб. У програмі необхідно використовувати рекурсію.

import random


def secret_number():
    numbers = list("1234567890")
    random.shuffle(numbers)

    if numbers[0] == "0":
        return secret_number()
    else:
        return "".join(numbers[:4])


def play(secret, attempts):
    guess = input("Guess a number: ")
    if len(guess) != 4:
        print("need 4 numbers")
        return play(secret, attempts)

    attempts += 1
    bull = 0
    cow = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bull += 1
        elif guess[i] in secret:
            cow += 1

    print("Bull:", bull)
    print("Cow:", cow)

    if bull == 4:
        print(f"you guessed the number in {attempts} attempts")
    else:
        play(secret, attempts)


secret = secret_number()
print(secret)
play(secret, 0)
