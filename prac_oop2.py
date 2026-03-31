# Завдання 1
# Створіть клас Проект з атрибутами:
# назва
# виділений кошторис
# загальні витрати
# чи завершений(за замовчуванням False)
# час виконання(за замовчуванням 0 місяців)
# список необхідних задач
# Додайте методи:
# вивід інформації: назва, час виконання, необхідні
# задачі
# добавити нову задачу
# розбити задачу на під-задачі: передається назва задачі
# та список під-задач
# виконати задачу, передається назва, час та ціна
# виконання
# поповнення кошторису

from typing import List
from typing import Dict

class Project:
    def __init__(self, name:str, budget:int):
        self.name = name
        self.budget = budget

        self.expenses:int = 0
        self.is_finish:bool = False
        self.time_of_processed:int = 0
        self.tasks:List[str] = []

    def show_info(self):
        print(f"Назва проекту: {self.name}")
        print(f"Час виконання: {self.time_of_processed} місяців")
        print(f" трати {self.expenses}")
        print(f" чи завершений {self.is_finish}")
        print(f"Необхідні задачі: {self.tasks}")


    def add_task(self, task:str):
        self.tasks.append(task)

    def decompose(self, task:str, ls_subtasks:List[str]):
        self.tasks.remove(task)
        self.tasks.extend(ls_subtasks)

    def do_task(self, task:str, time:int, cost:int):
        self.tasks.remove(task)
        self.time_of_processed += time
        self.expenses += cost

    def top_up_budget(self, amount:int):
        if amount > 0:
            self.budget += amount


project1 = Project('test', 10000)

project1.add_task("test task 1")
project1.add_task("test task 2 buy")

project1.decompose("test task 1", ['test', 'eat', 'close'])
project1.do_task("test", 1, 2000)
project1.top_up_budget(500)
project1.show_info()

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Phone:
    def __init__(self, max_memory:int, ):
        self.max_memory = max_memory

        self.used_memory:int = 0
        self.is_on:bool = False
        self.apps:Dict[str,int] = {}

    def show_info(self):
        print(f"Максимальний обсяг пам’яті: {self.max_memory} МБ")
        print(f"Зайнята пам’ять: {self.used_memory} МБ")
        print(f"Вільна пам’ять: {self.max_memory - self.used_memory} МБ")
        print(f"Стан телефону: {'увімкнений' if self.is_on else 'вимкнений'}")
        print(f"Встановлені додатки: {self.apps}")

    def delete_app(self, app:str, size:int):
        if app in self.apps:
            self.apps.pop(app)
            self.used_memory -= size

    def install_app(self, app:str, size):
        if self.max_memory - self.used_memory < size:
            print('not enough memory')
            return

        self.apps[app] = size
        self.used_memory += size

    def update_app(self, app:str, size:int):
        if app in self.apps:
            self.used_memory -= self.apps[app]
            self.apps[app] = size
            self.used_memory += size

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def open_app(self, app:str):
        if not self.is_on:
            print('phone is loked, turn on your phone before')
            return

        print(f"you open {app}")


phone1 = Phone(128)
phone1.install_app('instagram', 12)
phone1.install_app('yuotube', 30)
phone1.delete_app('yuotube', 30)
phone1.update_app('instagram', 13)

phone1.turn_on()
phone1.open_app('instagram')
phone1.turn_off()
phone1.show_info()
