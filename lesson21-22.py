import re # - данный модуль позволяет работать с регулярными выражениями

re_numbers = r"^\d+$"
re_numbers2 = r"\d+"
re_test = r"cat"
m = re.search(re_test, "a b c cat d") # - ищет перв=вое совпадение и возвращает
print(m)
print(bool(m))

re.match(re_test, "catapult")

print(re.fullmatch(re_numbers2, "123"))

#findall, finditer, sub, subn, split, compile

print(re.findall(r"\d+", "a1 b22 c333")) # - превращает в список

for n in re.finditer(r"\d+", "a1 b22 c333"): # - перебирает совпадения в цикле
    print(n)


text = re.sub(r"\s+", " ", "a b \n c") # - позволяет изменять находить по паттерну и изменять строку
print(text)

text = re.subn(r"\s+", " ", "a b \n c") # - говорит сколько замен сделал
print(text)

ls = re.split(r"[,\s;]+", "a, b;  c d")
print(ls)

rx = re.compile(r"\d+")
print(rx.findall("a1 b22 c333"))

# проверка номера телефона украині (+380)
# +380987654321, 380987654321, 0987654321
# +38(098) 765-43-21, 0 98 765 43 21, 380 98 7654321
RX_ALLOWED_CHARS = re.compile(r"^[0-9+\s()\-\t]+$")
RX_UA_PHONE = re.compile(r"^(380\d{9}|0\d{9})$")

line = "+38 (098) 765-43-21"
digits_only = re.sub(r"\D", "", line.strip())
print(digits_only)

if RX_ALLOWED_CHARS.fullmatch(line):
    is_correct = RX_UA_PHONE.fullmatch(digits_only)
    if is_correct:
        print("correct format")
    else:
        print("incorrect format")
else:
    print("incorrect format")
print(RX_UA_PHONE.fullmatch(digits_only))




# КОНТЕЙНЕРЫ И МАССИВЫ
# СПИСКИ - [] или list()

ls1 = [1,2,3, "a b c", True, print, list]
ls2 = list()

print(ls1, ls2)

ls = [5] * 3
print(ls)


ls = list("Hello")
print(ls)
print("".join(ls)) # - превращает список в строку

ls = ["Den", "John", "Doe", "Alice"] # - индексы "Den"- 0, "Alice" - -1
print(ls[0], ls[-1])
print(ls[::-1])

a, b, *x = ls # - распаковка
a, b, x, _ = ls

print(a, b, x)