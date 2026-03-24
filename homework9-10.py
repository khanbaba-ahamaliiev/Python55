# Завдання 1
# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма
# виводить на екран суму трьох чисел або добуток трьох чисел.


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

cal = input("Enter a choice(summa or dobutok): ")
if cal == "summa":
    print(f"summa {num1} + {num2} + {num3} = {num1 + num2 + num3}")
elif cal == "dobutok":
    print(f"dobutok {num1} x {num2} x {num3} = {num1 * num2 * num3}")
else:
    print("Please enter a valid choice")

# Завдання 2
# Користувач вводить з клавіатури три числа. Залежно від вибору користувача програма
# виводить на екран максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter another number: "))

action = input("Enter a choice(biggest, smallest or average): ")

biggest = 0
smallest = 0
average = 0

if num1 > num2:
    if num1 > num3:
        biggest = num1
        if num2 > num3:
            smallest = num3
        else:
            smallest = num2
    elif num1 < num3:
        biggest = num3
        smallest = num2
elif num1 < num2:
    if num1 < num3:
        smallest = num1
        if num2 < num3:
            biggest = num3
        else:
            biggest = num2
    elif num1 > num3:
        smallest = num3
        biggest = num2
else:
    print("Помилка")


if action == "biggest":
    print(f"максимум із трьох {biggest}")
elif action == "smallest":
    print(f"мінімум із трьох {smallest}")
elif action == "average":
    print(f"середньоарифметичне трьох чисел {(num1 + num2 + num3) / 3}")
else:
    print("Please enter a valid choice")

# Завдання 3
# Користувач вводить число, що представляє оцінку за шкалою від 1 до 5.
# Програма повинна вивести текстову інтерпретацію оцінки:
# Дуже погано.
# Погано.
# Задовільно.
# Добре.
# Відмінно.

mark = int(input("Enter a mark from 1 to 5: "))

if mark == 1:
    print("Дуже погано")
elif mark == 2:
    print("Погано")
elif mark == 3:
    print("Задовільно")
elif mark == 4:
    print("Добре")
elif mark == 5:
    print("Відмінно")
else:
    print("enter a valid choice")


# Завдання 4
# Користувач вводить з клавіатури кількість метрів. Програма має запропонувати кілька варіантів перекладу
# і, залежно від вибору користувача, перевести метри в одну або кілька одиниць виміру. Можливі варіанти:
# Перевести в одну з одиниць на вибір: милі, дюйми або ярди.
# Перевести одразу в усі три одиниці (милі, дюйми та ярди) і вивести результати для кожної.
# Перевести в кілометри та сантиметри, якщо користувач обирає цей варіант.

meters = int(input("Enter a number of meters: "))
question = int(
    input("""Виберіть один из вариантів(1, 2, 3):
1. Перевести в одну з одиниць на вибір: милі, дюйми або ярди
2. Перевести одразу в усі три одиниці (милі, дюйми та ярди)
3. Перевести в кілометри та сантиметри
""")
)
if question == 1:
    question1 = int(
        input("""виберіть(1, 2, 3):
    1. милі
    2. дюйми
    3. ярди """)
    )
    if question1 == 1:
        print(f"{meters} метрів це {meters / 1609.34} миль")
    elif question1 == 2:
        print(f"{meters} метрів це {meters * 39.3701} дюймів")
    elif question1 == 3:
        print(f"{meters} метрів це {meters * 1.09361} ярдів")
    else:
        print("помилка")
elif question == 2:
    print(
        f"{meters} метрів це \n{meters / 1609.34} миль \n{meters * 39.3701} дюймів \n{meters * 1.09361} ярдів"
    )
elif question == 3:
    print(
        f"{meters} метрів це \n{meters * 100} сантиметрів \n{meters / 1000} кілометри"
    )
else:
    print("помилка")

# Завдання 5
# Користувач вводить два числа і вибирає операцію (додавання, віднімання, множення, ділення, знаходження
# залишку, піднесення до степеня). Програма повинна виконати вибрану операцію і вивести результат.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operation = int(
    input(
        "Bибeріть операцію (1-6) 1. додавання, 2. віднімання, 3. множення, 4. ділення, 5. знаходження залишку, 6. піднесення до степеня: "
    )
)
if operation == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == 5:
    print(f"{num1} % {num2} = {num1 % num2}")
elif operation == 6:
    print(f"{num1} ** {num2} = {num1 ** num2}")
else:
    print("помилка")
# Завдання 6
# Користувач вводить тризначне число. Програма повинна визначити, чи всі цифри числа однакові.
# Якщо всі цифри однакові, вивести «Всі цифри однакові», інакше — «Цифри різні».
number = int(input("Enter a number: "))

n1 = number // 100
n2 = (number % 100) // 10
n3 = number % 10

if n1 == n2 and n2 == n3 and n3 == n1:
    print("Всі цифри однакові")
else:
    print("Цифри різні")
