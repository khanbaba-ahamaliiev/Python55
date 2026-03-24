# Завдання 1


def connector(dict1, dict2):
    new_dict = {}
    for key in dict1:
        new_dict[key] = dict1[key]

    for key in dict2:
        if key in new_dict:
            new_dict[key] += dict2[key]
        else:
            new_dict[key] = dict2[key]

    return new_dict


data1 = {"key1": 1, "key2": 2}
data2 = {"key2": 3, "key4": 4}

print(connector(data1, data2))


# Завдання 2
def reverser(dict):
    reverso_dict = {}
    for key, value in dict.items():
        reverso_dict[value] = key

    return reverso_dict


data = reverser({"key1": 1, "key2": 2})
print(data)

# Завдання 3
data = {}
while True:
    item = input("enter items name: ")

    if item == "":
        break

    price = int(input("enter item price: "))

    if item not in data:
        data[item] = price
    else:
        data[item] += price


print("\nТаблиця товарів:")
print(f"{'Товар':<15} | {'Ціна':>10}")
print("-" * 28)

total = 0

for name, price in data.items():
    print(f"{name:<15} | {price:>10.2f}")
    total += price

print("-" * 28)
print(f"{'Загальна ціна':<15} | {total:>10.2f}")

# Завдання 4


def text_converter(text, rate=False):
    word_count = {}

    for word in text.lower().split():
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    if rate:
        for key, value in word_count.items():
            word_count[key] = value / len(text) * 100

    return word_count


python = """Python is a popular programming language. Python is
 easy to learn and Python is powerful. Many developers use Python
  for web development, data analysis, and automation. Learning
  Python helps developers create useful programs."""

print(text_converter(python))


# Завдання 5


def add_student(groups, group_name, student_name):
    if group_name in groups:
        if student_name not in groups[group_name]:
            groups[group_name].append(student_name)
        else:
            print("Такий студент вже є у групі")
    else:
        print("Такої групи не існує")


def del_student(groups, group_name, student_name):
    if group_name in groups:
        if student_name in groups[group_name]:
            groups[group_name].remove(student_name)
        else:
            print("Студента немає у цій групі")
    else:
        print("Такої групи не існує")


def show_groups(groups):
    for group, students in groups.items():
        print(f"Група: {group}")
        print(f"Студенти: {students}\n")


student_groups = {
    "group101": ["anna", "mark", "olena", "ivan"],
    "group525": ["taras", "sofia", "maksym"],
    "group112": ["nazar", "daria", "andrii", "iryna"],
}

add_student(student_groups, "group525", "john")
del_student(student_groups, "group112", "daria")
show_groups(student_groups)

# Завдання 6


def ask_user():
    user_info = {}

    name = input("enter your name: ")
    age = int(input("enter your age: "))
    position = input("enter your position: ")

    user_info["name"] = name
    user_info["age"] = age
    user_info["position"] = position

    return user_info


def ask_another_users():
    five_users_info = {}

    for user in range(5):
        info = ask_user()
        five_users_info[info["name"]] = info

    return five_users_info


print(ask_another_users())
