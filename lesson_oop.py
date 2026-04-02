# ООП

# В программе нужно работать с обьектами, которые:
# они имеют определенную информацию
# они могут делать определенные действия

# Например:
# Аккаунт пользователя:
# Информация(Логин, имя, аватарка)
# Действия(зайти на сайт, верифицироваться, сделать заказ, ..)


# Класс - общиее описание того что умеют
class Dog:
    # идет описание атрибутов
    # идет описание методов

    # Инициализация (создание обьекта)
    # можно передать атрибуты
    # __init__
    def __init__(self, name, age, breed):
        # надо прикрепить атрибуты к self
        self.name = name.capitalize()
        self.age = age
        self.breed = breed.lower()


    # все методы создаются как функции
    # в методах 1 параметр всегда self
    def make_voice(self): # self - обьект который вызвал метод
        print(f"{self.name} makes wof")

    def show_info(self):
        print(f"DOG {self.name} {self.age} years old {self.breed}")

    def birthday(self):
        print(f"{self.name} happy birthday")
        self.age +=1

    def eat(self, food):
        print(f"{self.name} eat {food}")


# Обьекты класса
dog1 = Dog("barsik", 4, "haski")
dog2 = Dog("beethoven", 2, "labrador")
dog3 = Dog("john", 1, "simple")



dog2.make_voice()
dog1.make_voice()

dog3.show_info()

dog2.birthday()
dog2.show_info()

dog1.eat("meat")
