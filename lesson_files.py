filename = "test.txt"  # ищет в той же папке
# так же можно добавить путь в папке и абсолютный путь к файлу

file = open(filename)  # открывает файл

# print(file)
# print(type(file))

text = file.read()  # чтобы прочитать файл

print(text)
print(repr(text))


file.close()  # чтобы закрыть файл

# для избегания проблем с повреждением файла
# рекомендуют делать так:

# with open("test.txt") as file:
#           [code]


# прочитать файл как строки:
with open("test.txt") as file:
    lines = file.readlines()

print(lines)


# записать данные в файл
# mode - для чего открывать файл:
# w - для записи (если файла нет создаст и запишет данные, а если файл был то данные перезапишутся)
# r - для чтения(по умолчанию)
# a - для добавления(для существующего файла, чтобы дополнить)

with open("test.txt", "a") as file:
    file.write("\n")
    file.write("a big red fox")
