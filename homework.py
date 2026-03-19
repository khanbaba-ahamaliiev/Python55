# Завдання 5
# Є деякий текст. Реалізуйте таку функціональність
# • Змінити текст таким чином, щоб кожне речення починалося з великої літери;
# • Порахуйте скільки разів цифри зустрічаються в тексті;
# • Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# • Порахуйте кількість знаків оклику в тексті.
import re
text = "dmdv3md. vfvre. fdv4re rv1erv, vvr!"

def first_upper_letter(txt):
    result_text = ("")
    cap_next = True
    for letter in txt:
        if cap_next:
            result_text += letter.upper()
            cap_next = False
        else:
            result_text += letter
        if letter in ".?!; ":
            cap_next = True
    return result_text

def amount_of_numbers(txt):
    amount = 0
    for sym in txt:
        if sym.isdigit():
            amount += 1
    return amount

def amount_of_punctuation(txt):
    amount = 0
    for sym in txt:
        if sym in ".,:;-":
            amount += 1
    return amount

def amount_of_exclamation(txt):
    amount = 0
    for sym in txt:
        if sym in "!":
            amount += 1
    return amount

def main(txt):
    print(first_upper_letter(txt))
    print("кількість чисел", amount_of_numbers(txt))
    print("кількість знаків пунктуации", amount_of_punctuation(txt))
    print("кількість знаків оклику", amount_of_exclamation(txt))

main(text)
# Завдання 6
# Користувач з клавіатури вводить список цілих чисел. Необхідно видалити зі
# списку всі елементи, що повторюються, залишивши тільки унікальні. Результат вивести на екран.

ls = list(map(int, input("enter your list: ").strip().split()))
print(ls)

result = []
for n in ls:
    if n in result:
        continue
    else:
        result.append(n)

print(result)