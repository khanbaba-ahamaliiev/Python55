"""

модуль тестовый

"""

from math import pi


def get_circle_area(radius: float) -> float:
    """
    считает радиус круга

    :param radius: радиус круга
    :return: площадь круга
    """
    return pi * radius**2


def get_circle_perimetr(radius: float) -> float:
    """
    считает радиус круга

    :param radius: радиус круга
    :return: периметр круга
    """
    return 2 * pi * radius


if __name__ == "__main__":
    print("hello from modules")
    radius = float(input(" enter radius: "))

    res = get_circle_area(radius)
    print(res)
