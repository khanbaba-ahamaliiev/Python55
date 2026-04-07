# Магические методы

nums = [1,2,3,4,5]

# явный метод
nums.append(6)

# неявные методы
nums[0] # __getitem__
nums + [9,8,6] # __add__


num = 10

num + 5

res = num.__add__(5)
print(res)

class Person:
    def __init__(self, name:str, age:int): # __init__
        print("hello from __int__" )
        self._name = name
        self._age = age

    def __str__(self):  # __str__
        print("hello from __str__")
        return  f"Person named {self._name}, {self._age} yr"

    def __eq__(self, other):
        print("hello from __eq__")
        # other может быть любого типа данных
        if isinstance(other, Person):
            return self._name == other._name and self._age == other._age

        elif isinstance(other, str):
            return self._name == other

    def __gt__(self, other):
        print("hello from __gt__")

        if isinstance(other, Person):
            return self._age > other._age

        elif isinstance(other, str):
            return self._name == other

        raise TypeError(" you can't compare with other type")


person1 = Person('jorn', 18)
print(person1) # __str__


person2 = Person('mary', 27)
person3 = Person('mary', 27)


print(person1 == person2) # __eq__
print(person2 == person3)
print(person1 == 'jorn')

print(person1 > person3) # __gt__

class Cart:
    def __init__(self, items):
        self._items = items

    def __str__(self):
        return f"Cart items: {self._items}"

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __iter__(self):
        return iter(self._items)


cart = Cart(['milk', 'tofu', 'banana'])
print(cart)

# __contain__
print("milk" in cart)

# __getitem__
print(cart[0])

# __setitem__
cart[1] = 'kiwi'

# __iter__
for item in cart:
    print(item)

# yield как return, но не останавливает функцию
