import string

from unicodedata import name

print(string.whitespace)
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.printable)
print(string.digits)
print(string.punctuation)

import random
alphabet = string.ascii_letters + string.digits + string.punctuation
print("".join(random.choice(alphabet) for i in range(10)))


t1 = string.Template("Привет $name ваш заказ $code ") # string.Template - делает шаблоны, $ доллар нужен
print(t1.substitute(name="John", code="x1"))


f = string.Formatter() # - форматер


# f-string - строка с f (f"skk { }")
# t-string - новые строки (t"skk { }")
name = "Den"
line_f = f"skk {name}"
line_t = t"skk {name}"

print(line_f)
print(line_t)

print(line_t.values)
print(line_t.strings)
