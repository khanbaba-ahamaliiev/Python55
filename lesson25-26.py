# ФУНКЦИИ

# def название_функции (<параметры>):
# .... code
# .... <return>


# название_функции()


def foo():
    def inner_foo():
        print("inner foo")

    print("hello from foo")


# - переменные внутри функции можно использовать только внутри
foo()
foo()
foo()


def validate_n(n: str):
    if not (n1.isdigit() and 30 <= int(n1) <= 50):
        exit(-1)


n1 = "49"
validate_n(n1)
n2 = "40"
validate_n(n2)
n3 = "45"
validate_n(n3)
n4 = "50"
validate_n(n4)
n5 = "46"
validate_n(n5)

print("ok")


def foo(*x):  # * позволяет несколько цифр использовать
    print(x)
    print(sum(x))


foo(1, 2, 3)
foo(1, 3)
foo(1, 2, 3, 4, 5)


def boo(*args, **kwargs):
    print(args)
    print(kwargs)


boo(1, 2, 3, 4, 5, n1=1, n2=2, n3=3, n4=4, n5=5)


def action1():  # - функция пустышка
    pass


action1()


def ffoo(n1: int, n2: int) -> int:
    return (
        n1 + n2
    )  # - возвращает значение с функции и еще оно умеет выходить из функции


res = ffoo(5, 2)
print(res)
