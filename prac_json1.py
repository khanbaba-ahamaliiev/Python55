# Завдання 1
import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_new_user(data):
    user = input("Enter your login: ")
    password = input("Enter your password: ")

    if user in data:
        print("User with this login already exists.")
        return

    data[user] = password

def delete_user(data):
    user = input("Enter users login: ")
    if user not in data:
        print("User with this login does not exist.")
        return

    del data[user]

def change_password(data):
    user = input("Enter your login: ")

    if user not in data:
        print("User with this login does not exist.")
        return

    while True:
        password = input("Enter old password: ")

        if password == data[user]:
            new_password = input("Enter new password: ")
            data[user] = new_password
            break

def system_enter():
    data = load_data("data.json")

    while True:
        user = input("Enter your login: ")

        if user not in data:
            print("Wrong login")
            continue

        password = input("Enter your password: ")

        if password != data[user]:
            print("Wrong password")
            continue

        print("Welcome to system!")
        break

# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)

class Cart:
    def __init__(self, user:str):
        self._user = user

        self._total = 0
        self._items = []

    def add(self,item :str, price: int):
        self._items.append(item)
        self._total += price

    def delete(self, item: str, price: int):
        if item not in self._items:
            print("Item not exist")
            return

        self._items.remove(item)
        self._total -= price

    def info(self):
        print(f"user: {self._user}, total price: {self._total}")
        print(f"items: {self._items}")

    def save(self, filename:str = "cart.json"):
        data = {
            "user": self._user,
            "total": self._total,
            "items": self._items,
        }

        with open(filename, 'w',encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load(self, filename:str = 'cart.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self._user = data['user']
        self._total = data['total']
        self._items = data['items']


cart = Cart('John')
cart.load()
cart.info()
cart.add('orange', 70)
cart.delete('milk',100)
cart.save('cart.json')


# Завдання 3
size = '500x600'
color = 'grey'
button_color = 'bright grey'
placement_buttons = [100, 50]
instructions = ' be a good person'

def save_setting(filename:str = 'setting.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        data = {
            "size":size,
            "color":color,
            "button_color":button_color,
            "placement_buttons":placement_buttons,
            "instructions":instructions
        }

        json.dump(data, file, ensure_ascii=False, indent=2)

def load_setting(filename:str = 'setting.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def change_setting(data:dict):
    option = input("Change your setting: ")

    if option not in data:
        print("Wrong setting")
        return
    if option == 'placement_buttons':
        data[option] = input("enter new setting: ").split()
    else:
        data[option] = input("enter new setting: ")


def show_info(filename:str = 'setting.json'):
    data = load_setting(filename)
    new_data = json.dumps(data, indent=4, ensure_ascii=False)
    print(new_data)
