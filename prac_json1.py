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

        if user != data[user].keys():
            print("Wrong login")
            continue

        password = input("Enter your password: ")

        if password != data[user].keys():
            print("Wrong password")
            continue

        print("Welcome to system!")
        break
