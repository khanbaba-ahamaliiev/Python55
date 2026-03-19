# Завдання 1
people = set()

while True:
    person = input("Please enter your name: ")

    if person == "":
        break

    if person in people:
        print("That's a duplicate name!")
        continue

    people.add(person)

print(people)

# Завдання 2

def students_check(all_students, group1, group2):
    all_students = set(all_students)
    group1 = set(group1)
    group2 = set(group2)

    both = group1.intersection(group2)
    if len(both) != 0:
        print(f"студенти які є в двох групах одночасно: {both}")

    forgot = all_students - (group1 | group2)

    if len(forgot) != 0:
        print(f"студенти, про яких забули: {forgot}")

group1 = ["anna", "maria", "john", "alex", "kate"]

group2 = ["mike", "sara", "john", "david", "lisa"]

all_students = [
    "anna", "maria", "john", "alex", "kate",
    "mike", "sara", "david", "lisa", "tom", "emma"
]
students_check(all_students, group1, group2)

# Завдання 3

products = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
}

while True:
    product = input("Please enter your product: ").strip().lower()

    if product == "":
        break

    if product not in products:
        print("incorrect product")
        continue

    weight = float(input(f"Please enter {product} weight: "))

    if weight <= 0:
        print("invalid weight")
        continue

    print(f"{weight} kg of {product} cost {products[product]*weight} ")

# Завдання 4

vitamin_c = {
    "orange": 53,
    "lemon": 53,
    "kiwi": 92,
    "strawberry": 59,
    "apple": 5,
    "banana": 9,
    "broccoli": 89,
    "tomato": 14,
    "potato": 20,
    "pineapple": 48
}

diet = input("Please enter your diet: ").strip().lower().split(", ")

vit_count = 0
max_product = ""
max_vit = 0
for product in diet:
    if product in vitamin_c:
        vit_count += vitamin_c[product]

        if vitamin_c[product] > max_vit:
            max_product = product
            max_vit = vitamin_c[product]

print(f"вміст вітаміну С в раціоні {vit_count}")
print(f"Продукт з найбільшим вмістом вітаміну C: {max_product}")
print(f"Кількість вітаміну C: {vitamin_c[max_product]} мг")

Завдання 5

football_positions = {
    "воротар":1,
    "захисник":4,
    "півзахисник":4,
    "нападник":2
}

football_players = {
    "воротар":[],
    "захисник":[],
    "півзахисник":[],
    "нападник":[]
}

while True:
    players_position = input("Please enter your position: ").strip().lower()
    if players_position == "":
        break

    if players_position not in football_positions.keys():
        print("incorrect position")
        continue

    new_player = input("Please enter players name: ")
    if new_player == "":
        continue

    if new_player in football_players[players_position]:
        print("він вже в команді")
        continue

    if len(football_players[players_position]) == football_positions[players_position]:
        print("достатньо гравців на цій позиції")
        continue

    add = football_players[players_position].append(new_player)

    print(football_players)

