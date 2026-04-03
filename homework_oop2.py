# Завдання 3
from random import random

class Car:
    def __init__(self, brand, mileage, fuel_level, fuel_consumption, is_working=True):
        self._brand = brand
        self._mileage = mileage
        self._fuel_level = fuel_level
        self._fuel_consumption = fuel_consumption
        self._is_working = is_working

    def move(self, distance):
        if not self._is_working:
            print('car is not working')
            return

        self._mileage += distance
        self._fuel_level -= (distance * self._fuel_consumption) / 100

        if random() < 0.4:
            self._is_working = False
            print('car is broken')

    def repair(self):
        if not self._is_working:
            self._is_working = True
            print('car is working')

    def add_fuel(self, fuel):
        if self._fuel_level + fuel > 100:
            print('fuel exceeds 100 l')
        else:
            self._fuel_level += fuel


car = Car('toyota', 20000, 50, 9 )
car.move(10)
car.repair()
car.add_fuel(20)
