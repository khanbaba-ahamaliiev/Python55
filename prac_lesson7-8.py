def create_grid(size: int = 3) :
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або " " (пробіл для порожньої).
    """

    return [[" " for _ in range(size)] for _ in range(size)]
print(create_grid())

def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid - Поточна сітка гри.
    :return: None
    """
    print("    " + " | ".join(grid[0]))
    print(" ---+---+---")
    print("    " + " | ".join(grid[1]))
    print(" ---+---+---")
    print("    " + " | ".join(grid[2]))
board = create_grid()
print_grid(print_grid(board))




