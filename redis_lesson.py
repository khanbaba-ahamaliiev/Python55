from redis import Redis

# Подключение
host = "localhost"
port = 6379

server = Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True #чтобы возвращало не сырые данные
)

user_name = server.get("name")
print(user_name)

# server.set("name", "Alice")




# Завдання 2 Додавання ключа-значення
#  Використовуючи команду SET, додайте ключ "name" і
# значення "John Doe".

# server.set("name", "John Doe")

# Завдання 3 Отримання значення за ключем
#  За допомогою команди GET, отримайте значення ключа
# "name".

# server.get("name")

# Завдання 4 Додавання списку
#  Використовуючи команду RPUSH, додайте до списку
# "fruits" елементи "apple", "banana", "orange".

# server.rpush("fruits", "banana", "apple", "orange")

# Завдання 5 Отримання елементів списку
#  За допомогою команди LRANGE, отримайте всі елементи
# зі списку "fruits".


print(server.lrange("fruits", 0, -1))

# Завдання 6 Додавання хешу
# Використовуючи команду HMSET, додайте до хешу
# "user:1" поля "name" зі значенням "Alice" і "age" зі
# значенням 25.

# server.hmset("user:1", {"name": "Alice", "age": 25})

# Завдання 7 Отримання значень з хешу
# За допомогою команди HGETALL, отримайте всі поля
# та значення з хешу "user:1".

print(server.hgetall("user:1"))

# Завдання 8 Додавання елементу до множини
# Використовуючи команду SADD, додайте до множини
# "tags" елементи "red", "green", "blue".

# server.sadd("tags", "red", "green", "blue")

# Завдання 9 Отримання всіх елементів множини
# За допомогою команди SMEMBERS, отримайте всі
# елементи з множини "tags".

name = server.smembers("tags")
print(name)

# Завдання 10 Додавання лічильника
# Використовуючи команду INCR, додайте до лічильника
# "counter" одиницю.

# server.incr("counter", 20)


# Завдання 11 Отримання значення лічильника
# За допомогою команди GET, отримайте значення
# лічильника "counter".

print(server.get("counter"))

# Завдання 12 Видалення ключа
# Використовуючи команду DEL, видаліть ключ "name".

# server.delete("name")

# Завдання 13 Перевірка існування ключа
# За допомогою команди EXISTS, перевірте існування
# ключа "name".

print(bool(server.exists("name")))

# Завдання 14 Додавання значення з таймаутом
# Використовуючи команду SETEX, додайте ключ "message"
# зі значенням "Hello, Redis!" і таймаутом 60 секунд.

# server.setex("message", 5, "hello, Redis")
text = server.get("message")

print(text)


server.flushall()
