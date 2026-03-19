import random


user_data = input("enter numbers separated by a comma")
new_nums = []
if user_data == "":
    for _ in range(12):
        new_nums.append(random.randint(1, 10))
    print(new_nums)

else:
    nums = user_data.split(", ")

    new_nums = list(map(int, nums))
    print(new_nums)

print("сума чисел: ", sum(new_nums))

print("найбільше число: ", max(new_nums), "найменьше число: ", min(new_nums))

print("Перші 3 числа: ", new_nums[:3], "останні 3 числа: ", new_nums[-3:])

target = 7
count = 0
for num in new_nums:
    if num == target:
        count += 1

print("Кількість чисел 7: ", count)

for i, num in enumerate(new_nums):
    print(i, num)


students_name = ("jane", "john", "doe", "jack", "mary" )
while True:
    name_check = input("enter student name: ").lower()

    if name_check == "":
        break

    if name_check in students_name:
        print(f"{name_check} зареєстрований")
    else:
        print(f"{name_check} не зареєстрований")


movie_lib = (
    "gone with the wind",
    "casablanca",
    "12 angry men",
    "the godfather",
    "star wars: episode iv - a new hope",
    "back to the future",
    "titanic",
    "the lord of the rings: the fellowship of the ring",
    "the dark knight",
    "inception",
    "interstellar",
    "mad max: fury road",
    "parasite",
    "dune",
    "oppenheimer")



while True:

    movie_check = input("enter movie name: ").lower()

    if movie_check == "":
        break

    if movie_check in movie_lib[:5]:
        print(f"{movie_check} ретро-фільм")

    elif movie_check in movie_lib[6:10]:
        print(f"{movie_check} сучасний фільм")

    elif movie_check in movie_lib[-5:]:
        print(f"{movie_check} новий фільм")
    else:
        print("не правильна назва, спробуй ще раз")




def fruit_finder(tup, name):
    count_fr = 0

    name_check = name.lower()

    for fruit in tup:
        if name_check in fruit.lower():
            count_fr += 1


    return count_fr

print(fruit_finder(("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко"), "Яблуко" ))


def amount_numbers(tup):
    one_num = 0
    two_num = 0
    three_num = 0


    new_ls = list(map(str, tup))

    for num in new_ls:
        if len(num) == 1:
            one_num += 1
        elif len(num) == 2:
            two_num += 1
        elif len(num) == 3:
            three_num += 1

    print(f"""
    одноцифрових – {one_num} шт
    двоцифрових – {two_num} шт
    трицифрових – {three_num} шт""")

numbers = (3, 15, 7, 123, 88, 456, 9, 42, 100, 5)



amount_numbers(numbers)

items = tuple(input("enter your items: ").split(", "))
prices = tuple(input("enter your price: ").split(", "))

for item, price in zip(items, prices):
    print(item, price)


