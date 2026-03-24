# Документация


def get_greeting(name: str, age: int) -> str | None:
    """
    формирует и возвращает приветствие для пользователя

    Warning:
    Если параметры не правильные:
        * пустое имя
        * отрицательный возраст
        * имя с маленькой буквы
    то функция напишет предупреждение и вернет None

    :param name: str
    :param age: int
    :return: str
    """  # <--- docstring
    if age <= 0:
        print("age must be greater than 0")
        return None

    if name == "":
        print("name cannot be empty")
        return None

    if not name.istitle():
        print("first letter must be capitalized")
        return None

    greeting = f"Hello, {name}! You are {age} years old!"
    return greeting


greeting = get_greeting("John", 19)
print(greeting)


help(get_greeting)


def greet_users(users: list):
    """
    Выводит приветствие для каждого пользователя со списка

    см. get_greeting()

    :param users: list[list]
    :return:
    """

    for user in users:
        name = user[0]
        age = user[1]

        greeting = get_greeting(name, age)

        if greeting:
            print(greeting)


users = [["John", 46], ["Sophie", 35], ["Mary", 31], ["wmrovor", -10]]

greet_users(users)


# Хрестики нолики
# 1. создание сетки -- list[list[str]]
# 2. добавить новый элемент на сетку (получает координаты и получает символ)
# 3. спросить куда добавить символ
# 4. проверка кто выиграл


from typing import Literal

Symbol = Literal["X", "O"]
Cell = Literal["X", "O", " "]  # " " — порожня клітинка


def create_grid(size: int = 3) -> list[list[Cell]]:
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: int - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або " " (пробіл для порожньої).
    """

    return [[" " for _ in range(size)] for _ in range(size)]


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    size = len(grid)

    for i in range(size):
        print(" " + " | ".join(grid[i]) + " ")

        if i < size - 1:
            print("---+" * (size - 1) + "---")


def add_symbol_to_grid(
    grid: list[list[Cell]], row: int, col: int, symbol: Symbol
) -> bool:
    """
    Додає новий символ на сітку за вказаними координатами.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :param row: int - Індекс рядка (0-based).
    :param col: int - Індекс стовпчика (0-based).
    :param symbol: Symbol - Символ гравця ("X" або "O").
    :return: bool - True, якщо хід успішний (клітинка була вільна),
                    False, якщо клітинка вже зайнята або координати некоректні.
    """
    size = len(grid)

    if 0 <= row < size and 0 <= col < size:
        if grid[row][col] == " ":
            grid[row][col] = symbol
            return True

    return False


def ask_user_move(player_name: str, grid: list[list[Cell]]) -> tuple[int, int]:
    """
    Запитує у користувача, куди поставити новий символ.

    Повинна:
    - запитати координати (рядок і стовпчик),
    - перевірити, що клітинка вільна,
    - у разі помилки (зайнята/некоректна) — попросити ввести ще раз.

    :param player_name: str - Ім'я поточного гравця (наприклад, "Гравець X").
    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: tuple[int, int] - Пара (row, col) з коректними координатами для ходу.
    """
    size = len(grid)

    while True:
        row_input = input(f"{player_name}, введіть номер рядка (1-{size}): ")
        col_input = input(f"{player_name}, введіть номер стовпчика (1-{size}): ")

        if not row_input.isdigit() or not col_input.isdigit():
            print("Помилка! Потрібно ввести числа.")
            continue

        row = int(row_input) - 1
        col = int(col_input) - 1

        if not (0 <= row < size and 0 <= col < size):
            print("Координати поза межами поля.")
            continue

        if grid[row][col] != " ":
            print("Клітинка вже зайнята.")
            continue

        return row, col


def check_winner(grid: list[list[Cell]]) -> Symbol | None:
    """
    Перевіряє, чи є переможець на поточній сітці.

    Перевіряються:
    - усі рядки,
    - усі стовпці,
    - дві діагоналі (головна і побічна).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: Optional[Symbol] - "X", якщо виграв хрестик,
                                "O", якщо виграв нулик,
                                None, якщо переможця ще немає.
    """
    size = len(grid)

    for row in grid:
        if row[0] != " " and all(cell == row[0] for cell in row):
            return row[0]

    for col in range(size):
        column = [grid[row][col] for row in range(size)]
        if column[0] != " " and all(cell == column[0] for cell in column):
            return column[0]

    main_diag = [grid[i][i] for i in range(size)]
    if main_diag[0] != " " and all(cell == main_diag[0] for cell in main_diag):
        return main_diag[0]

    anti_diag = [grid[i][size - 1 - i] for i in range(size)]
    if anti_diag[0] != " " and all(cell == anti_diag[0] for cell in anti_diag):
        return anti_diag[0]

    return None


def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    for row in grid:
        for cell in row:
            if cell == " ":
                return True
        return False


def is_game_over(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи гра завершена.

    Гра завершується, якщо:
    - є переможець, або
    - немає вільних клітинок (нічия).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо гра завершена, False інакше.
    """

    if check_winner(grid) is not None or check_winner(grid) is not has_empty_cells(
        grid
    ):
        return True


def switch_player(player: Symbol) -> Symbol:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """

    return "O" if player == "X" else "X"


def main() -> None:
    """
    Головна функція. Організовує всю роботу гри та запускає програму.

    Алгоритм:
    1. Створити порожню сітку.
    2. Встановити стартового гравця (наприклад, "X").
    3. У циклі:
       - вивести сітку;
       - запитати хід у поточного гравця;
       - додати символ до сітки;
       - перевірити, чи є переможець;
       - перевірити, чи ще є вільні клітинки;
       - при завершенні гри вивести результат (хто виграв або нічия);
       - переключити гравця.
    """
    grid = create_grid()
    current_player: Symbol = "X"

    while True:
        print_grid(grid)

        row, col = ask_user_move(f"Гравець {current_player}", grid)
        add_symbol_to_grid(grid, row, col, current_player)

        winner = check_winner(grid)

        if winner:
            print_grid(grid)
            print(f"Переміг гравець {winner}!")
            break

        if not has_empty_cells(grid):
            print_grid(grid)
            print("Нічия!")
            break

        current_player = switch_player(current_player)


main()
