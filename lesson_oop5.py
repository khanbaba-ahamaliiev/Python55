# Наследование

class Parent:
    def __init__(self, name, age):
        print(f"parent hello __init__",)

        self._name = name
        self._age = age

    def display_info(self):
        print("parent hello from display_info")
        print(f"parent {self._name}, age {self._age}")


class Child(Parent): # Child наследует методы класса Parent
    def __init__(self, name, age, grade):
        # в дочерний класс часто появляется дополнительные атрибуты
        super().__init__(name, age)

        # дополнительная логика
        print(f"parent hello __init__")
        self._grade = grade

    def grow(self):
        self._age += 1

    def display_info(self): # перезагрузить родительский метод(изменить на свой)

        super().display_info() # если надо вызвать родительский вариант метода

        print("child hello from display_info")
        print(f"child {self._name}, age {self._age}, grade {self._grade}")





parent = Parent("John", 48)
parent.display_info()

child = Child("Bob", 12, 6)
child.grow()
child.display_info()
