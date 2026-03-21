# Завдання 1

with open("homework_files.txt", "r", encoding="UTF-8") as file:
    text = file.read().lower()
    print(text)

amount_sym = len(text)

amount_lines = len(text.splitlines())

amount_numbers = 0
for n in text:
    if n.isdigit():
        amount_numbers += 1

amount_vowels = 0
for v in text:
    if v in "аеїіоєяию":
        amount_vowels += 1

with open("homework_files_task1.txt", "w", encoding="UTF-8") as file:
    file.write(f"Кількість символів: {amount_sym}\n")
    file.write(f"Кількість рядків: {amount_lines}\n")
    file.write(f"Кількість цифр: {amount_numbers}\n")
    file.write(f"Кількість голосних літер: {amount_vowels}\n")

# Завдання 2

spec_word = input("enter your word: ")
filename = input("enter your filename.txt: ")

with open(filename, "r", encoding="UTF-8") as file:
    text = file.read().lower().replace("\n", "")
    print(text)

text_ls = text.split(" ")
amount_spec_word = 0
for w in text_ls:
    if w == spec_word:
        amount_spec_word += 1

print(f"Кількість {spec_word} у файлі {filename} : {amount_spec_word}")


# Завдання 3

with open("homework_files.txt", "r", encoding="UTF-8") as file:
    text = file.readlines()
    text = text[:-1]

with open("homework_files.txt", "w", encoding="UTF-8") as file:
    file.writelines(text)


