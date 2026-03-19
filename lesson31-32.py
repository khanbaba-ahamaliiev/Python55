# ЗАМЫКАНИЕ - (фишка пайтона) внутренняя функция запоминает значение внешней функции даже если та закончилась
# обязательно нужен return
def outer(k):

    def inner(x):
        return x * k

    return inner

inner_func = outer(5)
print(inner_func(10))



def make_counter(start=0):
    n = start

    def inc(step=1):
        nonlocal n
        n += step
        return n
    return inc

c = make_counter(10)
print(c())
print(c(2))
print(c(3))

c2 = make_counter()
print(c2())
print(c2())
print(c2())

# КЕРРИНГ - превращает функцию с несколькими параметрами в функции с одним параметром

def employee_review(employee):
    def handle(app):
        app_id, applicant, text = app

        if len(text) <10:
            return (app, employee, "regect","text too short")
        return (app, employee, "approve","goof")
    return handle

def manager_decision(manager):
    def handle(review):
        app, employee, decision, comment = review

        if decision == "approve":
            return (app, manager, "accept","good")
        return (app, manager, "reject","bad")
    return handle

def main():
    employee = 'den'
    manager = 'alice'

    applications = [[1, 'john', 'give me...'], [2, 'jane', 'give me...']]

    reviews = employee_review(employee)
    finalFn = manager_decision(manager)

    for app in applications:
        review = reviews(app)
        final = finalFn(review)

        app_id, applicant, text = app
        app2, employee, decision, comment = review
        app3, managerName, status, managerComment = final

if __name__ == '__main__':
    main()

# ДЕКОРАТОРЫ

# def hello():
#     print('hello')
#
# x = hello
# x()
import functools

def action(fn):
    @functools.wraps(fn) # -(модуль functools) показывает документацию функции
    def wrapper(name):
        print('before')
        fn(name)
        print('after')
    return wrapper

# def say():
#     print('hi')
#
# wrapper_say = action(say)
# wrapper_say()

@action # - @ спец символ декоратора
def say2(name):
    """print hi 2"""
    print('hi 2', name)

say2("den")
print(say2.__doc__)
print(say2.__name__)




def repeater(times):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeater(2)
def hi(name):
    print('hi', name)

hi('den')




def call_count(fn):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(fn.__name__, count, "times")
        return fn()
    return wrapper

@call_count
def ping():
    print('pong')

ping()
ping()
ping()




def action1(fn):
    def wrapper(*args, **kwargs):
        print('a1 before')
        fn(*args, **kwargs)
        print('a1 after')
    return wrapper

def action2(fn):
    def wrapper(*args, **kwargs):
        print('a2 before')
        fn(*args, **kwargs)
        print('a2 after')
    return wrapper

@action1
@action2
def ping2():
    print('pong')

ping2()

@functools.lru_cache # - кеширует
def add(a, b):
    return a + b

print(add(2,3))
print(add(2,3))
print(add(2,3))