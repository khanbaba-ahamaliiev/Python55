import datetime
from typing import List
# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть

class Message:
    def __init__(self, user:str, text:str, time:str):
        self._user = user
        self._text = text
        self._time =datetime.datetime.strptime(time,'%H:%M')

    def __str__(self):
        return f"user: {self._user}, text: {self._text}, time: {self._time.time()}"

    def __len__(self):
        return len(self._text)

    def __gt__(self, other):
        return self._time > other._time

mes = Message("John", "Hello World", "11:23")
mes2 = Message("John", "HOW ARE YOU", "12:40")
print(mes)
print(len(mes))

print(mes2 > mes)

messages = []
messages.append(Message("John", "Hello World", "11:23"))
messages.append(Message("John", "HOW ARE YOU", "12:30"))
messages.append(Message("John", "im fine", "07:40"))
messages.append(Message("John", "buy pizza", "23:16"))

# for message in messages:
#     print(message)

messages.sort()

for message in messages:
    print(message)

# Завдання 2

class Song:
    def __init__(self, name:str, author:str):
        self._name = name
        self._author = author

    def __eq__(self, other):
        return self._name == other._name and self._author == other._author

    def __str__(self):
        return f'song {self._name} by {self._author}'

song1 = Song("Love Me", "JMSN")
song2 = Song("7 Years", "Lukas Graham")
song3 = Song("Love Me", "JMSN")
song4 = Song("We Are The People", "Empire Of The Son")

print(song1)
print(song1 == song3)

class Playlist:
    def __init__(self, songs:List[Song]):
        self._songs = songs

    def __len__(self):
        return len(self._songs)

    def __contains__(self, song:Song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)

    def add_song(self, song:Song):
        self._songs.append(song)

    def remove_song(self, song:Song):
        self._songs.remove(song)

music = Playlist([song1, song2, song3])

print(len(music))
print(song1 in music)

music.add_song(song4)

for song in music:
    print(song)

music.remove_song(song2)


# Завдання 3
class Cart:
    def __init__(self, items:list, total:int):
        self._items = items
        self._total = total

    def __str__(self):
        return f"items: {self._items}, total: {self._total}"

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        return Cart(self._items + other._items, self._total + other._total)

car1 = Cart(['milk', 'butter', 'chocolate'], 120)
car2 = Cart(['apples', 'bananas', 'oranges'], 200)

print(car1)
print(len(car1))
print(car1 + car2)
