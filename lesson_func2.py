# Модули / библиотеки / фреймворки

# import [func]

#from [name] import [func]

import modules # - мой собственный модуль

area = modules.get_circle_area(10)
print(area)


import string_utils

text = "hi, What is your name? "
print(string_utils.delete_punc(text))

print(string_utils.sum_vowels(text))

print(string_utils.palindrome(text))


import math


def triangle_Square(a, b, angle):
    radians = math.radians(angle)
    S = 0.5 * (a * b) * math.sin(radians)
    return S

print(triangle_Square(3,4,45))
print(triangle_Square(3,4,90))


import time
def count_time(n=10):
    start = time.time()
    sum_num = 0
    for n in range(1, n+1):
        sum_num += n
    end = time.time()
    return end - start

print(count_time())