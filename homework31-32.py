# Фінансова звітність для різних організацій
# Щороку ваша компанія надає різним державним організаціям фінансову звітність.
# Залежно від організації формати звітності різні. Використовуючи механізм декораторів,
# вирішіть питання звітності для організацій.
import functools
def validate_data(data):
    year, income, expenses, profit, tax, tax_rate, net_profit = data

    if income < 0 or expenses < 0:
        print("Дохід або витрати не можуть бути від’ємними")

    return data


def report_for_tax(func):
    def wrapper(*args, **kwargs):
        data = validate_data(func(*args, **kwargs))
        year, income, expenses, profit, tax, tax_rate, net_profit = data

        return (
            f"[ПОДАТКОВА]\n"
            f"Рік: {year}\n"
            f"Дохід: {income:.2f}\n"
            f"Витрати: {expenses:.2f}\n"
            f"Прибуток: {profit:.2f}\n"
            f"Податок ({tax_rate * 100:.1f}%): {tax:.2f}\n"
            f"Чистий прибуток: {net_profit:.2f}\n"
        )
    return wrapper

def report_for_ministry(func):
    def wrapper(*args, **kwargs):
        data = validate_data(func(*args, **kwargs))
        year, income, expenses, profit, tax, tax_rate, net_profit = data

        return (
            f"[МІНІСТЕРСТВО]\n"
            f"Рік: {year}\n"
            f"Дохід: {income:.2f}\n"
            f"Витрати: {expenses:.2f}\n"
            f"Чистий прибуток: {net_profit:.2f}\n"
        )
    return wrapper


def report_for_statistics(func):
    def wrapper(*args, **kwargs):
        data = validate_data(func(*args, **kwargs))
        year, income, expenses, profit, tax, tax_rate, net_profit = data

        return (
            f"[СТАТИСТИКА]\n"
            f"Рік: {year}\n"
            f"Дохід: {income:.2f}\n"
            f"Витрати: {expenses:.2f}\n"
            f"Прибуток до оподаткування: {profit:.2f}\n"
        )
    return wrapper


def build_finance_report(year, income, expenses, tax_rate):  # [[1, 5000, 3000]]
    income = float(income)
    expenses = float(expenses)
    tax_rate = float(tax_rate)

    profit = income - expenses
    tax = max(0.0, profit) * tax_rate
    net_profit = profit - tax

    return [int(year), income, expenses, profit, tax, tax_rate, net_profit]


@report_for_ministry
def ministry_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


@report_for_statistics
def statistics_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


@report_for_tax
def tax_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


def main():
    year = 2026
    income = 1500000
    expenses = 900000
    tax_rate = 0.05

    print(ministry_report(year, income, expenses, tax_rate))
    print(statistics_report(year, income, expenses, tax_rate))
    print(tax_report(year, income, expenses, tax_rate))


if __name__ == '__main__':
    main()

# Аудит дій користувача
# У системі є функції, які виконують критичні операції (створення, видалення, зміна даних).
# Потрібно автоматично фіксувати в журналі хто виконав дію, яку саме дію, з якими параметрами і коли.
# Використовуючи декоратори, реалізуйте аудит для таких функцій.
from datetime import datetime


journal = []

def audit(func):
    def wrapper(*args, **kwargs):

        user = args[0]
        action = func.__name__
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = func(*args, **kwargs)

        record = f"{time} | Користувач: {user} | Дія: {action} | Параметри: {args[1:]}"
        journal.append(record)

        return result

    return wrapper


@audit
def create_data(user, data):
    print(f"Створено дані: {data}")


@audit
def delete_data(user, data_id):
    print(f"Видалено запис з ID: {data_id}")

@audit
def change_data(user, data, data_id):
    print(f"Дані з ID: {data_id} змінено: {data}")



def main():
    create_data("admin1", "Новий документ")
    delete_data("admin2", 101)
    change_data("admin3", "Звіт", 101)

    print("\nЖурнал аудиту:")
    for entry in journal:
        print(entry)


if __name__ == "__main__":
    main()


# Обмеження частоти запитів
# Ви розробляєте API, і деякі функції не можна викликати надто часто, щоб не
# перевантажувати систему. Потрібно обмежити кількість викликів однієї функції за певний проміжок
# часу для одного користувача. Використовуючи декоратори, реалізуйте rate limit для функцій.

import time

def rate_limit(max_calls, period):
    def decorator(func):

        count = 0
        start_time = 0

        def wrapper(user, *args):
            nonlocal count, start_time

            now = time.time()


            if start_time == 0:
                start_time = now


            if now - start_time > period:
                count = 0
                start_time = now


            if count >= max_calls:
                print("Ліміт перевищено!")
                return

            count += 1
            return func(user, *args)

        return wrapper
    return decorator


@rate_limit(4, 10)
def get_data(user):
    print(f"{user} отримав дані")


def main():
    for i in range(5):
        get_data("admin")
        time.sleep(2)


if __name__ == "__main__":
    main()
