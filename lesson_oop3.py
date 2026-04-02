# Принципы ООП

# Инкапсуляция
# Полиморфизм
# Наследование


# Инкапсуляция

class Person:
    def __init__(self, name, age):
        self._check_str(name)
        self._check_num(age)


        self._name = name # _ перед названим прячет агрумент
        self._age = age


    def _check_str(self, text):
        if text == '':
            print("str cant be empty")
            return

    def _check_num(self, num):
        if num <= 0:
            print("num cant be below 0")
            return

    def show_info(self):
        print("Name:", self._name)
        print("Age:", self._age)

    def get_grade(self, grade):
        self._check_num(grade)
        print("Grade:", grade)

person1 = Person("John", 23)
person1.show_info()



# Полиморфизм - в разных классах есть методы с одинаковым названием
#   которые одинаково реализуют логику

