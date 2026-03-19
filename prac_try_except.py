products = ["apple", "banana", "cherry", "milk"]

try:
    print(
        products[
            int(input("Please enter a index of product: "))
        ]
    )

except IndexError:
    print("error unexist")

except ValueError:
    print("error non float")

print("the end")


def ask_age():
    age = int(input("Please enter your age: "))
    if 0 < age:
        raise ValueError("invalid age, age can't be less than 0")

    if age > 130:
        raise ValueError("invalid age, age can't be greater than 130 years")

    return age


try:
    age = ask_age()
    print(f"{age = } years old")

except ValueError as e:
    print(f"error {e}")


def ask_number():
    number = input("Please enter a number: ")

    print(f"your number is {number = }")

    if number[:4] != "+380":
        raise ValueError("not a ukranian number")

    if len(number) != 11:
        raise ValueError("Please enter a number")

    return number


try:
    number = ask_number()
    print(f"your number is {number}")

except ValueError as e:
    print("error", e)


# Завдання 4
# Організуйте фільтр товарів в онлайн магазині. Усі товари
# діляться на певні категорії, причому один і той самий товар
# може відноситись до різних категорій. Є словник, де ключі –
# назви категорій, а значення – множини з товарами цієї
# категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які
# відносяться одночасно до цих двох категорій.
# Обробіть виняток коли категорії немає в словнику.
# Додатково: змініть код якщо користувач вводить декілька
# категорій.

catalog = {
    "смартфони": {"iPhone 15", "Samsung Galaxy S24", "Xiaomi 14"},
    "ноутбуки": {"MacBook Air", "Lenovo ThinkPad", "Asus ROG"},
    "аксесуари": {"чохол для телефона", "павербанк", "мишка USB", "iPhone 15"},
    "ігрові": {"Asus ROG", "PlayStation 5", "Xbox Series X"},
    "преміум": {"iPhone 15", "MacBook Air", "PlayStation 5"}
}

categories = input("Please enter a valid categories:").split(", ")

try:
    common_items = catalog[categories[0]]
    for category in categories:
        common_items = common_items & catalog[category]

    print(common_items)

except KeyError as e:
    print(f"Please enter a valid category {e}")
