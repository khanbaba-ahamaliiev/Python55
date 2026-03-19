# ОБЛАСТЬ ВИДИМОСТИ - используется правило LEGB.
# globals()  &  locals()

counter = 0
def foo():
    global counter # global
    counter += 1

foo()
foo()
print(counter)



def outer():
    counter = 0

    def inner():
        nonlocal counter # nonlocal
        counter += 1

    inner()
    inner()
    inner()

    print(counter)

outer()




ls = [print, input]



# def x(a, b, pow):
#     return (a+b)**pow
def action1(a, b):
    return a + b

def action2(a, b):
    return a * b

def action3(a, b):
    return a / b

def do_action(a, b, op):
    return op(a, b)

print(do_action(1, 2, action1))
print(do_action(14, 2, action2))
print(do_action(8, 2, action3))


# РЕКУРСИЯ - вызов функции внутри самой себя

    # в рекурсии должен быть всегда return
    # if

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))



ls = [1, [1,2], [[3], 5],[1],[[[5], 6]]]

def deep_sum(items):
    total = 0

    for item in items:
        if isinstance(item, list):
            total += deep_sum(item)
        elif isinstance(item, int):
            total += item
    return total

print(deep_sum(ls))


ls = ["a",["b" ,"c", ["d"]], "e"]

def print_nested(items, level=0):
    indent = "\t" * level
    for item in items:
        if isinstance(item, list):
            print(indent + "[")
            print_nested(item, level + 1)
            print(indent + "]")
        else:
            print(indent + str(item))

print_nested(ls)


