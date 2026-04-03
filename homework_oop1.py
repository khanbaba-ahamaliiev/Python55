
from typing import List


# Завдання 1
class Cart:
    def __init__(self, client:str, items:List[str]):
        self._client = client
        self._items = items

    def add_item(self, item:str):
        self._items.append(item)
        print(f"{item} added to cart.")

    def remove_item(self, item:str):
        if item in self._items:
            self._items.remove(item)
            print(f"{item} removed from cart.")

    def show_info(self):
        print(f"Client: {self._client}")
        print("Items in cart:")
        if self._items:
            for item in self._items:
                print(f"- {item}")
        else:
            print("Cart is empty")

cr1 = Cart('John', ['meat', 'milk', 'apple'])
cr1.add_item('juice')
cr1.remove_item('apple')
cr1.show_info()


# Завдання 2
class Phone:
    def __init__(self, number:str, battery_level:int):
        self._check_number(number)

        self._number = number
        self._battery_level = battery_level


    def _check_number(self, nums:str):
        if not nums.isdigit():
            print("Phone number is invalid.")
            raise ValueError

    def using(self, level:int):
        self._battery_level -= level

        if self._battery_level < 20:
            print("Battery level is too low.")

    def show_info(self):
        print(f"Phone number: {self._number}")
        print(f"Battery level: {self._battery_level}")

iphone=Phone('0671637558', 80)
iphone.using(20)
iphone.show_info()
