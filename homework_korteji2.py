# Завдання 1
# Користувач вводить через кому список товарів. Виведіть
# цей список на екран, але без повторень назв товарів
items = list(
    set(
        input('enter your items: '.lower()).split(", ")
    )
)

print(items)

# Завдання 2
# У магазині є два списки клієнтів: ті хто отримав знижкові
# купони, і ті хто ними скористався.
# Напишіть функцію, яка отримує 2 списки та виводить
# інформацію:
#  Імена тих, хто отримав купон, але не скористався,
# також вивести їх кількість
#  Імена шахраїв, які скористались знижкою, але магазин
# не давав їм купони

def clients_discount(earned_ls, used_ls):
    earned_discount = set(earned_ls)
    used_discount = set(used_ls)

    earned_nouse = earned_discount.difference(used_discount)
    scammers = used_discount.difference(earned_discount)

    print("Не скористались купоном:", list(earned_nouse), "Кількість:", len(earned_nouse))
    print("Шахраї:", list(scammers))

clients_with_coupons = ["anna", "ivan", "maria", "oleh"]
clients_used = ["ivan", "maria", "petro"]

clients_discount(clients_with_coupons, clients_used)
