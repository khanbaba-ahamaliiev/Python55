# Завдання 1
# Реалізуйте роботу банку. Усі дані зберігаються у
# словнику, де ключ – ім’я клієнта, значення – баланс на
# рахунку.
# Напишіть функцію, яка отримує словник з даними та
# зараховує гроші на баланс. Для цього вона запитує ім’я та
# суму у користувача, якщо користувача немає, то вносить його
# дані у словник, інакше додає суму до балансу.
# Напишіть іншу функцію, яка отримує словник з даними та
# знімає гроші з рахунку. Для цього вона запитує ім’я та суму у
# користувача, якщо користувача немає, то вивести відповідне
# повідомлення. Якщо на балансі не достатньо грошей, теж
# вивести повідомлення.
# Напишіть функцію main, яка організує роботу всієї
# програми, а саме матиме такий функціонал: поповнити
# рахунок, зняти кошти, завершити роботу


def deposit(data):
    name = input("enter user name: ")
    if name == "":
        print("error incorrect name")
        return

    money = float(input("enter money: "))
    if money == 0 or money < 0:
        print("error incorrect money")
        return

    if name in data:
        data[name] += money
    else:
        data[name] = money

def withdraw(data):
    name = input("enter user name: ")

    if name == "":
        print("error incorrect name")
        return

    if name not in data:
        print("name is not found")
        return

    money = float(input("enter money: "))

    if money > data[name]:
        print("not enough money")
        return
    else:
        data[name] -= money

def main():
    bank_data = {}

    while True:
        option = input("enter option(1-deposit, 2-withdraw, 3-exit): ")
        if option == "1":
            deposit(bank_data)

        elif option == "2":
            withdraw(bank_data)

        elif option == "3":
            break

        else:
            print("option not found")

        print(bank_data)
if __name__ == '__main__':
    main()