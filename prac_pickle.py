import json
import pickle


def add_new_item(items:list[str]):
    new_item = input('add new item: ')
    items.append(new_item)
    print(new_item, "added.")


def show_items(items:list[str]):
    print("items:")
    for item in items:
        print(f"\t{item}")


def save_items_json(items:list[str]):
    with open('items.json', 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)


def load_items_json():
    with open('items.json', 'r') as file:
        return json.load(file)


def save_items_pickle(items:list[str]):
    with open('items.pkl', 'wb') as file:
        pickle.dump(items, file)

def load_items_pickle():
    with open('items.pkl', 'rb') as file:
        return pickle.load(file)

items  = []

add_new_item(items)
add_new_item(items)

save_items_json(items)
save_items_pickle(items)

items_json = load_items_json()
items_pickle = load_items_pickle()



# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.


class Student:
    def __init__(self, name:str, specialization:str, grades:list[int]):
        self._name = name
        self._specialization = specialization
        self._grades = grades

    def add_grade(self, grade:int):
        self._grades.append(grade)
        print(f'{grade} added.')

    def show_info(self):
        print(f"name: {self._name}")
        print(f"specialization: {self._specialization}")

        print(f"avarage grades: {self._get_avarage_grade()}")

    def _get_avarage_grade(self):
        if len(self._grades) == 0:
            return None

        avarage = sum(self._grades)/len(self._grades)
        return avarage

    def save_json(self, filename:str="student.json",):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(self._get_state_dict(), file, indent=4)

    def _get_state_dict(self):
        return {
            'name' : self._name,
            "specialization" : self._specialization,
            "grades" : self._grades
        }

    def _set_state_dict(self, state_dict:dict):
        self._name = state_dict['name']
        self._specialization = state_dict['specialization']
        self._grades = state_dict['grades']

    def load_json(self, filename:str="student.json"):
        with open(filename, 'r') as file:
            state_dict = json.load(file)

        self._set_state_dict(state_dict)

    def save_pkl(self, filename:str="student.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(self._get_state_dict(), file)

    def load_pkl(self, filename:str="student.pkl"):
        with open(filename, 'rb') as file:
            state_dict = pickle.load(file)

        self._set_state_dict(state_dict)



student1 = Student('John', 'IT', [10, 9, 8])
student2 = Student('Jane', 'Lawer', [10, 6, 8])
student3 = Student('Марія', 'Management', [7, 9, 8])

student1.add_grade(8)
student2.add_grade(9)

student1.show_info()
student2.show_info()
student3.show_info()

student1.save_json("student1.json")
student2.save_json("student2.json")
student3.save_json('student3.json')

student1.save_pkl('student1.pkl')
student2.save_pkl('student2.pkl')
student3.save_pkl('student3.pkl')

student1.load_json("student1.json")
student2.load_json("student2.json")
student3.load_json('student3.json')

student1.load_pkl('student1.pkl')
student2.load_pkl('student2.pkl')
student3.load_pkl('student3.pkl')

student1.show_info()
student2.show_info()
student3.show_info()



# Завдання
# Є словник з друзями, де ключ - людина, а значення -
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.

def add_friends(friends:dict[str, list[str]]):
    friend1 = input('enter a name: ')
    friend2 = input('enter a name: ')

    if friend1 not in friends:
        friends[friend1] = []
    if friend2 not in friends:
        friends[friend2] = []

    friends[friend1].append(friend2)
    friends[friend2].append(friend1)


def save_friends_json(friends:dict[str], filename:str="friends.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(friends, file, indent=4, ensure_ascii=False)

def load_friends_json():
    with open('friends.json', 'r') as file:
        return json.load(file)

def save_friends_pickle(friends:dict[str], filename:str="friends.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(friends, file)

def load_friends_pickle():
    with open('friends.pkl', 'rb') as file:
        return pickle.load(file)

friends = dict()
add_friends(friends)

save_friends_json(friends)
fr_json = load_friends_json()
print(fr_json)

save_friends_pickle(friends)
fr_pkl = load_friends_pickle()
print(fr_pkl)



# Реалізуйте телефонну книгу.
# Контакт містить:
# ім’я
# телефон
# email
# Функціонал:
# додати контакт
# видалити контакт
# знайти контакт за ім’ям
# показати всі контакти
# зберегти/завантажити через json
# зберегти/завантажити через pickle


def add_contact(phone_book:dict[str, dict[str, str]]):
    name = input('enter a name: ')
    phone = input('enter a phone: ')
    email = input('enter a email: ')

    phone_book[name] = {
        'phone': phone,
        'email': email
    }
    return phone_book

def delete_contact(phone_book:dict[str, dict[str, str]], name:str):
    if name in phone_book:
        del phone_book[name]

def find_contact(phone_book:dict[str, dict[str, str]], name:str):
    if name in phone_book:
        name, info = phone_book[name].items()
        return name, info

    print(f'{name} not found')

def show_all_contacts(phone_book:dict[str, dict[str, str]]):
    for name, info in phone_book.items():
        print(f'{name} phone: {info["phone"]} email: {info["email"]}')

def save_json(phone_book, filename:str="contacts.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(phone_book, file, indent=4, ensure_ascii=False)

def load_json(filename:str="contacts.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_pickle(phone_book, filename:str="contacts.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump([phone_book], file)

def load_pickle(filename:str="contacts.pkl"):
    with open(filename, 'rb') as file:
        return pickle.load(file)
