# Завдання 1
import random


users_nums = {1,20,13,4,18,16,7,9,12,2}
nums = set(random.randint(1,20) for _ in range(10))
print(nums)


print(f"""Максимальне {max(users_nums)}, мінімальне число {min(users_nums)}, 
кількість чисел {len(users_nums)}""")

print(f"""Унікальні числа, введені користувачем,
яких немає серед випадкових {users_nums.difference(nums)}""")

print(f"""Спільні числа, введені користувачем, 
які є серед випадкових {users_nums.intersection(nums)}""")

print(f"""Усі числа, які є або в одній або 
в іншій множин {users_nums.union(nums)}""")



# Завдання 2

def invite_guests(guests_ls, event):
    guests = set(guests_ls)
    for guest in guests:
        print(f"{guest} запрошуємо на {event}")

guests = [
    "Наталія", "Тарас", "Світлана", "Роман",
    "Наталія", "Петро", "Юрій", "Світлана",
    "Людмила", "Андрій", "Тарас"
]

event = "Новорічна вечірка"

invite_guests(guests, event)

# Завдання 3

def shopping_lists(product_list1, product_list2):
    first_product = set(product_list1)
    second_product = set(product_list2)

    common_product = first_product.intersection(second_product)
    print(f"Товари, які можна купити разом: {common_product}")

    only_first_product = first_product.difference(second_product)
    print(f"Товари, які потрібні лише першій людині: {only_first_product}")

    only_second_product = second_product.difference(first_product)
    print(f"Товари, які потрібні лише другій людин: {only_second_product}")

person1 = [
        "Молоко", "Хліб", "Яйця", "Сир",
        "Масло", "Яблука", "Кава", "Хліб"
]

person2 = [
        "Хліб", "Яйця", "Чай", "Цукор",
        "Молоко", "Банани", "Кава", "Чай"
]

shopping_lists(person1, person2)

# Завдання 4

def conference_guests(registered_ls, payed_ls, confirmed_ls):
    guests = set(registered_ls)
    payed_guests = set(payed_ls)
    confirmed_guests = set(confirmed_ls)

    reg_nopayed_guests = guests.difference(payed_guests)
    print(f"Імена тих, хто зареєструвався, але не оплатив участь {reg_nopayed_guests}")

    conf_noreg_guests = confirmed_guests.difference(guests)
    print(f"Імена тих, хто підтвердив присутність, але не  зареєстрований {conf_noreg_guests}")

    payed_noconf_guests = payed_guests.difference(confirmed_guests)
    print(f"Імена тих, хто оплатив участь, але не підтвердив присутність {payed_noconf_guests}")

    reg_payed_guests = guests.intersection(payed_guests)
    print(f"Імена тих, хто зареєструвався і оплатив участь {reg_payed_guests}")

    all_check = guests.intersection(payed_guests).intersection(confirmed_guests)
    print(f"Імена тих хто пройшов усі 3 етапи {all_check}")

registered = [
    "Андрій", "Марія", "Олег", "Ірина",
    "Софія", "Дмитро", "Олег", "Наталія",
    "Владислав", "Марія"
]

paid = [
    "Марія", "Олег", "Ірина", "Тарас",
    "Софія", "Оксана", "Олег", "Ірина"
]

confirmed = [
    "Марія", "Софія", "Дмитро", "Андрій",
    "Оксана", "Юлія", "Марія"
]

conference_guests(registered, paid, confirmed)


# Завдання 5

def manager_check(workers1, workers2, workers3, all_workers):
    workers1 = set(workers1)
    workers2 = set(workers2)
    workers3 = set(workers3)
    all_workers = set(all_workers)

    working_emp = workers1.union(workers2).union(workers3)
    lost_workers = all_workers - (working_emp)
    print(f"імена всіх, про кого забули {lost_workers}")

    both_group12 = workers1.union(workers2)
    both_group23 = workers2.union(workers3)
    both_group13 = workers3.union(workers1)

    both_workers = both_group12.intersection(both_group23).intersection(both_group13)
    print(f"співробітникі, які опинились у двох групах {both_workers}")

all_employees = [
    "Андрій", "Марія", "Олег", "Ірина",
    "Софія", "Дмитро", "Наталія",
    "Владислав", "Оксана", "Тарас"
]

group1 = [
    "Андрій", "Марія", "Олег", "Ірина"
]

group2 = [
    "Софія", "Дмитро", "Наталія", "Олег"
]

group3 = [
    "Владислав", "Оксана"
]

manager_check(group1, group2, group3, all_employees)