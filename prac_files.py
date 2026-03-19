# Завдання 1

with open("test.txt", encoding="UTF-8") as file:
    text = file.read()

print(len(text))
print(text.count("\n"))

# Завдання 2

filename = input("Enter file name: ")
name = input("Enter a name: ")
age = int(input("Enter your age: "))

with open(filename+".txt", "w") as file:
    file.write(f"{name} is {age} years old")

# Завдання 3

with open("test.txt", encoding="UTF-8") as file:
    text = file.read()

with open("new.txt", "w", encoding="UTF-8") as file:
    file.write(text)

# Завдання 4

letter = input("Enter a letter: ")
filename = input("Enter a filename.txt: ")

with open(filename, encoding="utf-8") as file:
    text = file.read()

count_l = 0
for word in text.lower().split():
    if word[-1] == letter:
        count_l += 1

print(count_l)

# Завдання 5

with open("test.txt", encoding="UTF-8") as file:
    text = file.read()

new_text = ""

for sym in text:
    if sym == "*":
        new_text += "&"

    elif sym == "&":
        new_text += "*"

    else:
        new_text += sym


with open("test.txt", "w", encoding="UTF-8") as file:
    file.write(new_text)

# Завдання 6

def add_numbers(text, numbers):
    numbers = [str(num) + "\n" for num in numbers]
    with open(text, "a", encoding="UTF-8") as file:
        file.write(f"{numbers}")

def read_file(filename):
    with open(filename, encoding="UTF-8") as file:
        text = file.read()
        numbers = text.split("\n")
        return numbers

add_numbers("test.txt", [1, 2, 3, 4, 5])

print(read_file("test.txt"))
