# 19. Система входу
# Задайте логін і пароль у коді. Введіть їх з клавіатури. Виведіть "Вхід успішний" або
# "Помилка".
# Підказка: Перевіряйте обидві умови одночасно через and.

login = 'test'
password = 'test123'

your_login = input("enter your login: ")
your_password = input("enter your password: ")

if login == your_login and password == your_password:
    print("Вхід успішний")
else:
    print("Помилка")

# 20. Пора року
# Введіть номер місяця (1–12). Виведіть відповідну пору року

number_month = int(input("enter a number of month: "))

if number_month <= 2 or 12:
    print("its winter")

elif number_month <= 5:
    print("its spring")

elif number_month <= 8:
    print("its summer")

elif number_month <= 11:
    print("its autumn")

else:
    print("wrong number")


# 27. Кількість введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть кількість введених чисел
# (без нуля).
# Підказка: Використайте лічильник count, збільшуйте після кожного введення.
# 28. Сума введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть суму всіх введених чисел
# (без нуля).

count = 0
sum_numbers = 0
while True:
    number = int(input("enter a number: "))

    if number != 0:
        count += 1
        sum_numbers += number

    else:
        break

print(f"спроб було: {count}")
print(f"сума чисел: {sum_numbers}")


# 37. Кратні числа
# За допомогою for порахуйте, скільки чисел від 1 до 100 кратні 7.
count = 0

for n in range(1, 100):
    if n % 7 == 0:
        count += 1

print(f"чисел від 1 до 100 кратні 7: {count}")

# 91. Словник учня
# Створіть словник з даними учня: ключі "ім'я", "вік", "клас". Виведіть кожне поле
# окремим рядком.
student = dict()

student['name'] = input("enter a student name")
student['age'] = int(input("enter a student age"))
student['class'] = input("enter a student class")

print(student)

# 5. Клас Movie — фільм
# Атрибути: назва (str), жанр (str), рейтинг (float, від 0 до 10).
# Метод display(): виводить усі дані про фільм.
# Метод update_rating(r): оновлює рейтинг. Перевіряйте діапазон 0–10.

class Movie:
    def __init__(self, title: str, genre: str, rating: float):

        self.title = title
        self.genre = genre

        if 0 <= rating <= 10:
            self.rating = rating
        else:
            print("error")
            self.rating = 0

    def display(self):
        print(f" name: '{self.title}' \n genre: {self.genre} \n rating: {self.rating}/10")

    def update_rating(self, r: float):
        if 0 <= r <= 10:
            self.rating = r
            print(f"rating of movie: '{self.title}' updated to {self.rating}.")
        else:
            print("error")
