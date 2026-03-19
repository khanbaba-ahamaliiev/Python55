# Словари - сохраняет данные парами и без индексов - {ключ:значение}

    # значение может быть что угодно
    # ключи сохраняются в множестве

        # Последствия:
            # 1. не может быть дубликатов
            # 2. нету порядка
            # 3. ключи хешируются и нельзя использовать изменяемые типы данных(list, set, dict)


data = {
    "Mary": 1000,
    "John": 800,
    "Bob": 300,
}

client = "Mary"
balance = data[client] # - чтобы получить значение ключа

print(balance)

print(data["Mary"])
print(data["John"])


data["John"] += 200
print(data["John"])



data = {"хлеб": 30, "яблоки": 65}

data["хлеб"] = 35 # изменить значение
print(data)

data["молоко"] = 80 # добавить новую пару
print(data)

data.pop("хлеб") # удалить пару
print(data)



for items in data: # получаем ключи
    print(items)

print(data.values()) # чтобы получить только значения

for price in data.values():
    print(price)

for item, price in data.items(): # чтобы получить пары
    print(item, price)

if "молоко" in data: # проверка есть ли ключ в словаре
    print("yes")
else:
    print("no")



# ЗАДАЧКА С РАБОТНИКАМИ
def create_worker_info():
    worker_info = {}

    worker_info["name"] = input("enter worker's name: ")
    worker_info["salary"] = int(input("enter worker's salary: "))
    worker_info["experience"] = int(input("enter worker's experience: "))

    return worker_info

# info = create_worker_info()
#
# print(info)


def create_workers(workers_num=3):
    workers = []
    for i in range(workers_num):
        worker = create_worker_info()
        workers.append(worker)

    return workers

# workers = create_workers()
# print(workers)

# import json # - делает красиво
# print(workers)
# print(json.dumps(workers, indent=2))


def increase_salary(workers, bonus, min_exp=2):
    for worker in workers:
        if worker["experience"] > min_exp:
            worker["salary"] += bonus

workers = create_workers(workers_num=3)
increase_salary(workers, bonus=250)
print(workers)


