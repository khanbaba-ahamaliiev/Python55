# Завдання 1

def get_password():
    password = input("Enter a password: ")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    if len(set(password)) != len(password):
        raise ValueError("Password must be unique")

    return password

try:
    get_password()
    print("Password is valid")

except ValueError as e:
    print("Password is invalid")
    print(e)


# Завдання 2

users_info = {
    "user":"password",
    "khan":"12345678",
    "ivan":"ivan123"
}

def check_user():
    login = input("Enter a login: ")

    if login not in users_info:
        raise ValueError("Login does not exist")

    password = input("Enter a password: ")

    if password != users_info[login]:
        raise ValueError("Password does not match")

try:
    check_user()
    print("Password is valid")

except ValueError as e:
    print("Password is invalid")
    print(e)