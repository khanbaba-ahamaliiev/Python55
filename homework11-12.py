#
# Завдання 1
# Написати програму, яка за вибором користувача зводить введене ним число
# у ступінь від нульового до сьомого включно.

number = int(input("введіть число:"))
power = int(input("введіть степінь: "))
if 0 <= power <= 7:
    print(f"число {number} у степені {power} буде {number ** power}")
else:
    print("помилка")
# Завдання 2
# Написати програму підрахунку вартості розмови для різних мобільних
# операторів. Користувач вводить вартість розмови і вибирає з якого на який
# оператор він телефонує. Вивести вартість на екран.

lifecell = 1
vodafone = 1.4
kievstar = 1.2

from_op = input("виберіть оператора з якого телефонуєте (lifecell, vodafone, kievstar): ")
to_op = input("виберіть оператора на який телефонуєте (lifecell, vodafone, kievstar): ")
duration = int(input("Введіть тривалість розмови в хвилинах: "))

if from_op == "lifecell":
    print(f"вартість складатиме {lifecell * duration} грн")
elif from_op == "vodafone":
    print(f"вартість складатиме {vodafone * duration} грн")
elif from_op == "kievstar":
    print(f"вартість складатиме {kievstar * duration} грн")
else:
    print("помилка")

# Завдання 3
# Користувач вводить із клавіатури число в діапазоні від 1 до 100. Якщо число
# кратне 3 (ділиться на 3 без залишку) потрібно вивести слово Fizz. Якщо число
# кратне 5 потрібно вивести слово Buzz. Якщо число кратне 3 і 5 потрібно
# вивести Fizz Buzz. Якщо число не кратне не 3 і 5 потрібно вивести саме
# число. Якщо користувач ввів значення не в діапазоні від 1 до 100 потрібно
# вивести повідомлення про помилку.

number = int(input("введіть число від 1 до 100: "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"ваше число {number}")
else:
    print("помилка")

# Завдання 4
# Зарплата менеджера становить 200$ + відсоток від продажів, продажі до 500$
# – 3%, від 500 до 1000 – 5%, понад 1000 – 8%. Користувач вводить із
# клавіатури рівень продажів для трьох менеджерів. Визначити їхню зарплату,
# визначити найкращого менеджера, нарахувати йому премію 200$, вивести
# підсумки на екран.

sales_from_manager1 = int(input("рівень продажів 1 менеджера: "))
sales_from_manager2 = int(input("рівень продажів 2 менеджера: "))
sales_from_manager3 = int(input("рівень продажів 3 менеджера: "))

if sales_from_manager1 < 500:
    per_manager1 = 0.03
elif sales_from_manager1 <= 1000:
    per_manager1 = 0.05
elif sales_from_manager1 > 1000:
    per_manager1 = 0.08
else:
    print("error")

if sales_from_manager2 < 500:
    per_manager2 = 0.03
elif sales_from_manager2 <= 1000:
    per_manager2 = 0.05
elif sales_from_manager2 > 1000:
    per_manager2 = 0.08
else:
    print("error")

if sales_from_manager3 < 500:
    per_manager3 = 0.03
elif sales_from_manager3 <= 1000:
    per_manager3 = 0.05
elif sales_from_manager3 > 1000:
    per_manager3 = 0.08
else:
    print("error")

salary_manager1 = 200 + sales_from_manager1 * per_manager1
salary_manager2 = 200 + sales_from_manager2 * per_manager2
salary_manager3 = 200 + sales_from_manager3 * per_manager3

if salary_manager1 > salary_manager2 and salary_manager1 > salary_manager3:
    salary_manager1 += 200
    print(f"Найкращий менеджер 1\n зарплата 1 менеджера: {salary_manager1}\n зарплата 2 менеджера: {salary_manager2}\n зарплата 3 менеджера: {salary_manager3}")
elif salary_manager2 > salary_manager3:
    salary_manager2 += 200
    print(f"Найкращий менеджер 2\n зарплата 1 менеджера: {salary_manager1}\n зарплата 2 менеджера: {salary_manager2}\n зарплата 3 менеджера: {salary_manager3}")
else:
    salary_manager3 += 200
    print(f"Найкращий менеджер 3\n зарплата 1 менеджера: {salary_manager1}\n зарплата 2 менеджера: {salary_manager2}\n зарплата 3 менеджера: {salary_manager3}")
# Завдання 5
# Користувач вводить суму кредиту і термін (у роках). Програма визначає
# процентну ставку і розраховує загальну суму до виплати:
# Для кредиту до 10 000$ на строк до 3 років – ставка 8%.
# Для кредиту до 10 000$ на строк понад 3 роки – ставка 10%.
# Для кредиту від 10 001$ до 50 000$ на строк до 3 років – ставка 12%.
# Для кредиту від 10 001$ до 50 000$ на строк понад 3 роки – ставка 15%.
# Для кредиту понад 50 000$ на будь-який термін – ставка 20%.
# Програма виводить підсумкову суму до виплати і щомісячний платіж.

credit = int(input("введіть суму кредиту: "))
period = int(input("введіть термін кредиту(у роках): "))

if credit <= 10000 and period <= 3:
    credit_per = 0.08
elif credit <= 10000 and period > 3:
    credit_per = 0.10
elif credit <= 50000 and period <= 3:
    credit_per = 0.12
elif credit <= 50000 and period > 3:
    credit_per = 0.15
elif credit > 50000:
    credit_per = 0.20

total_credit = credit * ((1 + credit_per) ** period)
month_pay = total_credit / (period * 12)
print(f"підсумкова суму до виплати {total_credit} і щомісячний платіж {month_pay}")
# Завдання 6
# Ви розробляєте програму для розрахунку вартості комплексного обіду в
# ресторані. Меню складається з трьох категорій: закуска, основна страва і
# десерт. Залежно від вибору клієнта і його статусу програма повинна
# розрахувати підсумкову вартість з урахуванням можливих знижок і спеціальних
# пропозицій.
# Умови:
# Меню комплексного обіду.
# Закуски:
# Салат – 5$,
# Суп – 7$.
# Основні страви:
# Курка – 10$,
# Риба – 12$.
# Десерти:
# Морозиво – 3$,
# Фрукти – 4$.
# Знижки.
# Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт),
# надається знижка 10% на все замовлення.
# Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
# Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з
# іншими знижками.
# Спеціальні пропозиції.
# Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
# Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається
# безкоштовний напій (наприклад, "Чай").
# Підсумкова вартість.
# Програма повинна коректно застосувати всі знижки та спеціальні
# пропозиції, а потім розрахувати підсумкову вартість замовлення.

salad = 5
soup = 7
chicken = 10
fish = 12
icecream = 3
fruits = 4

discount = 0

meal1 = int(input("виберіть закуски(0-2): \n0.Нічого \n1.Салат – 5$ \n2.Суп – 7$  "))
meal2 = int(input("виберіть основні страви(0-2): \n0.Нічого \n1.Курка – 10$ \n2.Риба – 12$."))
meal3 = int(input("виберіть Десерти(0-2): \n0.Нічого \n1.Морозиво – 3$, \n2.Фрукти – 4$."))

status = int(input("ви постійний клієнт(1) чи ви у нас вперше(2): "))
if 0 <= meal1 <= 2 and 0 <= meal2 <= 2 and 0 <= meal3 <= 2:
    if meal1 == 0:
        meal1 = 0
    elif meal1 == 1:
        meal1 = salad
    else:
        meal1 = soup
    if meal2 == 0:
        meal2 = 0
    elif meal2 == 1:
        meal2 = chicken
    else:
        meal2 = fish
    if meal3 == 0:
        meal3 = 0
    elif meal3 == 1:
        meal3 = icecream
    else:
        meal3 = fruits
else:
    print("error")

total_price = meal1 + meal2 + meal3

if meal1 != 0 and meal2 != 0 and meal3 != 0:
    discount += 0.1
    if total_price >= 20:
        discount += 0.05
if status == 1:
    discount += 0.05

free_drink = 0
if meal1 == soup and meal2 == fish and meal3 != 0:
    meal3 -= 2
elif meal2 == chicken and meal3 == icecream:
    free_drink = 1

last_price = (meal1 + meal2 + meal3) * (1-discount)
print(f"загальна вартість зі знижкою складає {last_price}")
if free_drink == 1:
    print("до вашого замовлення додався безкоштовний напій")
