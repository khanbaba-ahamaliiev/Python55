# потоковое(параллельное) программирование


# в программировании есть задачи:
# CPU - задачи
# IO - задачи (input-output -- ввод-вывод) - это когда процессор ждет на ответ сайта

# name = input() #  IO
# result = func(name) # CPU
# print(result)


#   Асинхронность - это когда мы не ждем ответа от сайта,
# а выполняем другие задачи, а когда ответ придет,
# то обрабатываем его

# в программирование есть асинхронные функции

# многопроцессорность - multiprocessing

# многопоточность - threading




# обычный код
import time

def long_func():
    total = 0
    for i in range(50000):
        total += i

    time.sleep(1)

start = time.time()
long_func()
long_func()
end = time.time()
print("время выполнения", end - start) # примерно 2 секунды


# ПОТОКИ
import threading

thread1 = threading.Thread(target=long_func)
thread2 = threading.Thread(target=long_func)

start = time.time()

thread1.start() # запускаем потоки
thread2.start() # не ждет завершение прошлого потока

thread1.join() # ждем завершение потока, если не вызвать, то программа может завершиться раньше, чем поток закончит работу
thread2.join()

end = time.time()
print("время выполнения", end - start) # примерно 1 секунда

# def print_text(text):
#     for _ in range(100):
#         print(text)
#
#
# thread1 = threading.Thread(target=print_text, args=('hello',)) # args - аргументы для функции
# thread2 = threading.Thread(target=print_text, kwargs={'text': 'world'}) # kwargs - аргументы для функции
#
# thread1.start()
# thread2.start()
