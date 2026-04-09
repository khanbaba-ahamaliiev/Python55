from abc import ABC, abstractmethod
from typing import List
from enum import Enum


class Stat(Enum):
    intelligence = 'intelligence'
    strength  = 'strength'
    dexterity = 'dexterity'
    mana = 'mana'
    defense = 'defense'

class Character(ABC):
    def __init__(
            self,
            name:str,
            max_hp:int,
            intelligence:int,
            strength:int,
            dexterity:int,
            mana:int,
            defence:int,
            level: int = 1,
    ):

        self._name = name
        self._max_hp = max_hp
        self._level = level
        self._hp = max_hp
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defence = defence

    @abstractmethod
    def attack(self) -> int:
        raise NotImplementedError

    def take_damage(self, damage:int):
        attaked = damage - self._defence

        if attaked > 0:
            self._hp -= attaked

    def level_up(self):
        if self._level <= 20:
            self._level += 1

    def increased_stat(self, stat:Stat):
        if stat == Stat.intelligence:
            self._intelligence += 1
        elif stat == Stat.strength:
            self._strength += 1
        elif stat == Stat.dexterity:
            self._dexterity += 1
        elif stat == Stat.mana:
            self._mana += 1
        elif stat == Stat.defense:
            self._defence += 1

    def rest(self):
        self._hp = self._max_hp

    def heal(self, heal_hp):
        self._hp += heal_hp
        if  self._hp > self._max_hp:
            self._hp = self._max_hp

# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):

    def attack(self) -> int:
        self._mana -= 5

        if self._mana <= 0:
            self._mana = 0
            return self._strength
        else:
            return 4 * self._strength

    def shield(self):
        self._defence -= 4 + self._level

    def unshield(self):
        self._defence -= 4 + self._level

    def heal_ally(self, ally:Character):
        heal_hp = 5 + 2 * self._level + 0.5 * self._mana
        ally.heal(heal_hp)


character = Paladin("Paladin", 5, 5, 5, 5, 5, defence=1)
character.take_damage(5)

# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence

class Mage(Character):
    def attack(self) -> int:
        if self._mana > 3:
            self._mana -= 3
            return 3 * self._intelligence + 4
        else:
           return 0

    def fireball(self) -> int:
        if self._mana > 5:
            self._mana -= 5
            return 2 * self._intelligence + 3
        else:
            return 0

    def heal_ally(self, ally: Character):
        heal_hp = 3 + self._level + 3 * self._intelligence
        ally.heal(heal_hp)


class Warrior(Character):
    def attack(self):
        return 4 * self._strength + 3

    def power_strike(self, enemies:List[Character]):
        for enemy in enemies:
            if self._level > enemy._level:
                enemies.remove(enemy)

class Rogue(Character):
    def attack(self):
        return self._strength + self._level
