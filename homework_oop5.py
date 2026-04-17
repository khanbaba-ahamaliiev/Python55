from abc import ABC, abstractmethod


class Pet(ABC):

    def __init__(self, name, satiety=50, energy=50):
        self._name = name
        self._satiety = satiety
        self._energy = energy

    def sleep(self):
        self._energy = 100

    def eat(self, food_amount):
        self._satiety += food_amount

        if self._satiety > 100:
            self._satiety = 100

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass

class Cat(Pet):

    def play(self, activity_level):
        if self.satiety > 60:
            self._energy -= 2 * activity_level

    def make_sound(self):
        print('Мяу')

    def catch_mouse(self):
        mouse = 20

        if self.energy > 30:
            print('зловила мишу')

            if self.satiety > 40:
                print('грається з мишею')

            else:
                self.eat(mouse)

class Dog(Pet):
    def play(self, activity_level):
        if self._satiety > 15:
            self._energy -= activity_level / 2
            self._satiety -= activity_level / 2

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self._satiety > 10:
            print('поймал мяч')
            self._energy -= 5
