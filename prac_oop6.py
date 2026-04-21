# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off
from abc import ABC, abstractmethod
from enum import Enum
from uuid import uuid4
from typing import List


class Status(Enum):
    on = 'on'
    off = 'off'
    working = 'working'

class CleanMode(Enum):
    wet = 'wet'
    dry = 'dry'

class Robot(ABC):
    def __init__(
            self,
            name: str = None,
            battery_level: int = 100,
            status: Status = Status.off,
    ):
        if name is None:
            self._name = str(uuid4())
        else:
            self._name = name
        self._battery_level = battery_level
        self._status = status

    def info(self):
        print(f'Name: {self._name}, \nBattery Level: {self._battery_level}%, \nStatus: {self._status.value}')

    def charge(self):
        self._battery_level = 100

    def turn_on(self):
        self._status = Status.on

    def turn_off(self):
        self._status = Status.off

robot1 = Robot()
robot1.info()


class CleaningRobot(Robot):
    def __init__(
            self,
            name: str = None,
            battery_level: int = 100,
            status: Status = Status.off,
            dust_capacity: int = 0,
            water_capacity: int = 100,
            cleaning_mode: CleanMode = CleanMode.wet,
    ):
        super().__init__(name, battery_level, status)
        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity
        self._cleaning_mode = cleaning_mode

    def info(self):
        super().info()
        print(f"dus_capacity: {self._dust_capacity}, \nwater_capacity: {self._water_capacity}")
        print(f"Cleaning mode: {self._cleaning_mode}")

    def turn_on(self):
        if self._dust_capacity == 100:
            print('контейнер для пилу повний')
            return

        if self._water_capacity == 0 and self._cleaning_mode == CleanMode.wet:
            print('нема води для вологого прибирання')
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0

    def fill_water(self):
        self._water_capacity = 100

    def swap_mode(self):
        if self._cleaning_mode == CleanMode.wet:
            self._cleaning_mode = CleanMode.dry
        else:
            self._cleaning_mode = CleanMode.wet

    def clean(self, energy:int, dust:int, water=None):
        if self._dust_capacity <= dust:
            raise ValueError('нема місця для пилу')

        self._dust_capacity += dust

        if self._cleaning_mode == CleanMode.wet:
            if water is None:
                print('нема води')
                return
            if self._water_capacity <= water:
                raise ValueError('немає достатньо місця для води')

            self._water_capacity -= water

        self._battery_level -= energy

# Завдання 3
# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити
# об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів(gun,
# knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки
# на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний
# предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки
# middle
# o якщо це небезпечний предмет, то рівень
# небезпеки high
# Рівень небезпеки не може стати нижчим
class AlertLevel(Enum):
    low = 'low'
    middle = 'middle'
    high = 'high'


class DangerousItems(Enum):
    knife = 'knife'
    gun = 'gun'
    bat = 'bat'


class SecureRobot(CleaningRobot):
    def __init__(
            self,
            min_speed: int,
            alert_level: AlertLevel,
            dangerous_items: List[DangerousItems] = None,
            name: str = None,
            battery_level: int = 100,
            status: Status = Status.off,
    ):
        super().__init__(name, battery_level, status)
        self._min_speed = min_speed
        self._dangerous_items = dangerous_items
        self._alert_level = alert_level
        if self._dangerous_items is None:
            self._dangerous_items = []
        else:
            self._dangerous_items = dangerous_items

    def info(self):
        super().info()
        print(f"min_speed: {self._min_speed}, \nalert_level: {self._alert_level}")
        print(f"dangerous_items: {self._dangerous_items}")

    def turn_off(self):
        if self._status == Status.on:
            self._alert_level = AlertLevel.low
            super().turn_off()
