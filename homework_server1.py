# Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

import threading

def input_number(numbers):
    while True:
        num = input('enter number: ')
        if num == "":
            break
        numbers.append(int(num))

def sum_numbers(numbers):
    print(f"summa: {sum(numbers)}")

def avg_numbers(numbers):
    print(f"average: {sum(numbers) / len(numbers)}")

numbers = []
thread_input = threading.Thread(target=input_number, args=(numbers,))

thread_input.start()
thread_input.join()

thread_sum = threading.Thread(target=sum_numbers, args=(numbers,))
thread_avg = threading.Thread(target=avg_numbers, args=(numbers,))

thread_sum.start()
thread_avg.start()
