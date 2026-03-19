# fcf - означает что функция віступает обьектом 1 класса

# hof - функции высшего порядка

# side effects

# lambda аргументы: выражение

def doo(ls, op):
    temp = []
    for i in ls:
        temp.append(op(i))
    return temp

ls = [1, 2, 3, 4, 5]

# def exp(n):
#     return n if n == 1 else n * exp(n - 1)

new_ls = doo(ls, lambda n: n*3)# - делает тоже самое что и функция
print(new_ls)



# map, filter, zip, sorted

#map() - применяет функцию к каждому элементу списка

ls = [1, 2, 3, 4, 5]

res = list(map(lambda n: n*3, ls))
print(res)


ls = ["  Alex  ", "!@John ", "__Den"]

res = list(map(lambda n: n.strip(" !@_"), ls))
print(res)

# filter()

ls = [1, 2, 3, 4, 5]
res = list(filter(lambda n: n % 2 == 0, ls))
print(res)

# zip() - обьеденяет элементы

ls1 = [ "den", "john", "bob"]
ls2 = [ "den@g.com", "john@g.com", "bob@g.com"]
ls3 = [ "+380494", "+380302", "+38039032", "+380aa"]
res = list(zip(ls1, ls2, ls3))
print(res)

import functools

ls = [1, 2, 3, 4, 5]
res = functools.reduce(lambda acc, x: acc+x, ls) # -
print(res)

def foo(acc, x):
    if isinstance(x, int):
        return acc + x
    return acc
ls = ["1", 2, print, 3, 4]
res = functools.reduce(foo , ls, 0) # - аккамулирует
print(res)

def power(base, exp):
    return base ** exp

power_exp4 = functools.partial(power, exp=4) # - замораживает параметр в функции
print(power_exp4(2))
print(power_exp4(3))

functools.wraps() # - нужна, чтобы получить метаданные функции
functools.lru_cache()







