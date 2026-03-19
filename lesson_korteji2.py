# множества

fruits = {"apple", "banana", "cherry"}
print(fruits)

nums = [1,2,3,4,5,6,7]
nums = set(nums)
print(nums)

# пустое множество

empty = {} # не множество, а считает словарем
print(type(empty))

empty = set() # только так можно сделать пустое множество
print(type(empty))


# Минусы множества:

# 1. нету индексов
# 2. нету повторений
# 3. нельзя добавлять элементы что меняются


# Методы множеств
fruits = {"apple", "banana", "cherry"}

fruits.add("orange") # добавляет элемент
print(fruits)

fruits.discard("orange") # удаляет элемент (как remove(но он выдает ошибку когда нет элемента который хотите удалить))
print(fruits)


# Операции с множествами
workers = ["Анна", "Олег","Ігор","Олег","Анна","Марія","Сергій","Олег"]
special_workers = ["Анна","Ігор","Вікторія"]

workers = set(workers) # перевели в множества
special_workers = set(special_workers)

all_workers = workers.union(special_workers) # объединение множеств
# all_workers = workers | special_workers - тоже самое
print(all_workers)

no_special_workers = workers.difference(special_workers) # разница множеств
# no_special_workers  = workers - special_workers - тоже самое
print(no_special_workers)

both = workers.intersection(special_workers) # пересечение множеств
# both = workers & special_workers - тоже самое
print(both)

