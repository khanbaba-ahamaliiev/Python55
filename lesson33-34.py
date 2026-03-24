# КОРТЕЖИ - не изменяются

s = (1, 2, 3, 4)
print(s[2])

s = ()

t = 5, 4, 3, 2, 1


t = (1, 2, [1, 2, 3])
t[2][0] = 5
print(t)

print(len(t))
print(2 in t)


a = (1, 2)
b = (3, 4)

print(a + b)
print(a, b)
print(a * 3)


def foo():
    name = "alex"
    age = 20
    return name, age


user = foo()
print(user)
name, age = foo()
print(name, age)


db = ("user1", "user2", "user3", "user4")
ls_db = list(db)
db_t = tuple(ls_db)  # конвертирует в кортеж и обратно
print(list(db))

# МНОЖЕСТВА -нету индексации

users = {1}
ls = [1, 2, 3, 3, 3, 3, 3]
users = set(ls)
print(users)

ls = [n for n in range(1, 10)]
users = set(ls)
print(users)
print(len(users))
print(5 in users)


users = {"Den", "Alex", "Bob", "Alice", "John"}

user = users.pop()  # удаляет последний элемент
print(user)

users2 = users.copy()
print(users2, users)
print(id(users2), id(users))

# users.remove("Den")
# users.add("Den")

a = {1, 2, 3}
b = {3, 4, 5}

res = a.intersection(b)
print(res)
# res = a.intersection_update(b)
# print(a)


res1 = a.difference(b)
res2 = b.difference(a)
print(res1, res2)

# a.difference_update(b)
# print(a)

# res = a.union(b)
# print(res)
c = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(a.issubset(c))
print(c.issubset(a))
print(a.issuperset(c))
print(c.issuperset(a))

fs = frozenset(c)
print(len(fs), 5 in fs)
