# Занятие 5-6

print("Hello World", "python", 2+2)
print("Hello World","python", 2+2,  sep="-") # sep="" - сепаратор между слов можно знак вместо пробела
print("Hello World","python", 2+2,  end="<") # end="" - в конце ставит знак, после него нового рядка не будет
print("Hello Students")


# escape

# \n - новая линия
print("Hello \nStudents")
# \t - табуляция - tab
print("Hello \t\t\tStudents")
# \" - двойные кабычки в тексте
print("Hello \"Students\"")
# \' - одинарные кавычки в тексте
print("Hello \'Students\'")
# \\ - backslash
print("\\Hello\\ students")
# \r - возврат в начало
print("Hello \rStudents")
# \b - удаляет прошлую букву
print("Hell\bo Studen\bts")


print("""   
   76 g
      x
""") # три раза кавычки-прямая речь



print(0.3+0.3+0.3)
print(0.1+0.1)


# + - * / - база
# // % **
#// - без остатка (откидывает)
# % - остаток от деления


name = "john"
age = 25
print("Name:", name, "age:", age)
print (f"Name: {name}, age: {age}") #одно и тоже


n1 = 5
n2 = 10
print("n1 + n2 =", n1 + n2)
print(f"{n1} + {n2} = {n1 + n2}")

#calculator
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
calc = num1 + num2
print(f"your result is: {calc}")