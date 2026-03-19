# Завдання 1. Фільтрація та нормалізація списку покупок
# Є список рядків, де значення можуть бути в різному форматі, з пробілами, у різному регістрі.
# Вхід:
# items = ["  Milk  ", "bread", "BREAD", "", "  eggs", "Eggs ", "   ", "cheese"]
# Вимоги:
# Очистити пробіли по краях (map)
# Викинути порожні рядки після очищення (filter)
# Нормалізувати регістр: зробити все у нижньому регістрі (map)
# Прибрати дублікати, зберігши порядок появи
# Повернути фінальний список
# Очікуваний результат:
# ["milk", "bread", "eggs", "cheese"]

items = ["  Milk  ", "bread", "BREAD", "", "  eggs", "Eggs ", "   ", "cheese"]
clear_space = list(map(lambda n: n.strip(), items))
print(clear_space)
clear_nothing = list(filter(lambda n: n != "", clear_space))
print(clear_nothing)
make_lowercase = list(map(lambda n: n.lower(), clear_nothing))
print(make_lowercase)

result = []
for n in make_lowercase:
    if n in result:
        continue
    else:
        result.append(n)

print(result)

# Завдання 2. Вищі функції: фабрика фільтрів для студентів
# Є список студентів у вигляді словників.
# Вхід:
# students = [
#     {"name": "Іра", "age": 17, "avg": 91, "has_debt": False},
#     {"name": "Петро", "age": 19, "avg": 73, "has_debt": True},
#     {"name": "Оля", "age": 18, "avg": 88, "has_debt": False},
#     {"name": "Максим", "age": 20, "avg": 60, "has_debt": False},
# ]
# Вимоги:
# Написати вищу функцію make_student_filter(min_avg, max_age, no_debts_only)
# яка повертає функцію-предикат predicate(student) -> bool
# За допомогою filter відібрати студентів, які:
# мають середній бал >= min_avg
# мають вік <= max_age
# якщо no_debts_only=True, то has_debt має бути False
# За допомогою map отримати список імен відібраних студентів
# Додати параметр name_startswith (літера або None), якщо задано,
# фільтрувати ще і за першою літерою імені
# Приклад:
# min_avg=80, max_age=18, no_debts_only=True
# Результат: ["Іра", "Оля"]
def min_avg(lst):
    min = 100
    for i in lst:
        if i["avg"] < min:
            min = i["avg"]
        else:
            continue
    print(min)
    return min

def max_age(lst):
    max = 0
    for i in lst:
        if i["age"] > max:
            max = i["age"]
        else:
            continue
    print(max)
    return max

def no_debts_only(lst): #
    while True:
        for i in lst:
            if i["debts"] == "False":
                continue
            else:
                return False


# def make_student_filter(min_avg, max_age, no_debts_only):



students = [
    {"name": "Іра", "age": 17, "avg": 91, "has_debt": False},
    {"name": "Петро", "age": 19, "avg": 73, "has_debt": True},
    {"name": "Оля", "age": 18, "avg": 88, "has_debt": False},
    {"name": "Максим", "age": 20, "avg": 60, "has_debt": False}
    ]
min_avg(students)
max_age(students)


# Завдання 3. Пайплайн обробки даних: застосуйте список трансформацій
# Є список чисел, де треба побудувати обробку як конвеєр з кроків. Кроки задаються як функції.
# Вхід:
# nums = [1, -2, 3, 0, 4, -5, 10, 11, 12]
# Вимоги:
# Створити функції-трансформації:
# only_positive (filter): залишає > 0
# only_even (filter): залишає парні
# square (map): підносить до квадрату
# Створити вищу функцію apply_pipeline(data, steps):
# steps це список кортежів виду ("map", func) або ("filter", func)
# функція проходить по steps і застосовує відповідний map або filter
# Викликати пайплайн:
# positive -> even -> square
# Повернути список результатів
# Очікуваний результат:
# позитивні: [1, 3, 4, 10, 11, 12]
# парні: [4, 10, 12]
# квадрат: [16, 100, 144]

nums = [1, -2, 3, 0, 4, -5, 10, 11, 12]