# СТРОКИ

name = "John"  # immutable - неизменная строка

print(ord("A"))  # - возвращает 1 символ в число
print(chr(66))  # - преобразует число в символ

# for i in range(126):
#     print(f"{i} - {chr(i)}")

name_code = name.encode()  # .encode() - для кодирования данных
print(name_code)

name_decode = name_code.decode()  # .decode() - для декодирования данных
print(name_decode)


line = "Hello World!"
print(line)

l1 = line[3]  # - чтобы выбрать символ из строки
print(l1)
print(len(line))  # - показывает длину строки

print(line[-2])  # - python поддерживает обратную индексацию

# line[start:stop:step] start - начальный элемент stop - последний step - необязательный шаг

print(line[0:5], line[:5])
print(line[5:], line[5:11])  # - одно и тоже
print(line[::2], line[::1])  # - 1.берет каждый второй элемент и 2.повторяет строку

id(line)  # - показыввает id переменной

print(line[::-1])  # - сделает строку задом на перед


# 1 регистр
print("hello world".capitalize())  # - делает 1 букву большую в 1 слове
print("hello world".title())  # - делает все отдельные слова с большой буквы
print("Hello wOrLd".lower())  # - делает все буквы маленькими
print("hello world".upper())  # - делает все буквы большими
print("hello world, Straße ".casefold())  # - работает как .lower() но для других языков

# trim
print(
    "    Hello wOrLd    ".lower().strip()
)  # - можно подряд несколько методов использовать
print("   hello world   ".strip())  # -убирает пробелы по краям

print(
    "   hello world   ?@#".strip("?@#")
)  # - если в скобки добавить символы то оно убирает символы по бокам
# .lstrip() i rstrip() - выбирает с какой стороны убирать

print("hello world.txt".removesuffix(".txt"))
print("+39080700650".removeprefix("+390"))

# search

print("banana".find("na"))  # - ищет в слове и возвращает индекс
# .rfind() - ищет справа на лево

print("banana".index("na"))  # - тоже ищет, но выдает ошибку если не найдет
# .rindex()

print("banana".count("na"))
print(
    "banana".startswith("na")
)  # true of false начинается ли строка из того что в скобках
print("banana".endswith("na"))  # true of false заканчивается ли строка

# transf
print("I love java".replace("java", "python"))  # - меняет строку на другое

# split
print("I love java".split())  # - превращает строку в тип списка (розбивает по пробелам)
print("I.love.java".rsplit(".", 1))  # - то же самое но справа на лево
print("I\nlove \njava".splitlines())  # - делает по новым рядам

# " ".join([  ]) - превращает список в строку

print("hi".center(30, "*"))
print("hi".ljust(30, "*"))
print("hi".rjust(30, "*"))
print("7".zfill(3))


# format

name = "John"
age = 19
print(f"{name} hi!")
print(f"{name} hi!, age {age}")
print(f"{name} hi!, age {age}")

price = 34
print(f" Price = {price:.2f}")

# bool method

print("123abc".isalnum())  # .is
print("123abc".isalpha())
print("123abc".isascii())
# . . . . . . . .

# r"" - игнорирует \
