import threading
import json

# Завдання 1
def find_min(nums, result):
    result['min'] = min(nums)

def find_max(nums, result):
    result['max'] = max(nums)

nums = list(map(int, input("enter numbers ").split(', ')))
result = {}

thread1 = threading.Thread(target=find_min, args=(nums, result))
thread2 = threading.Thread(target=find_max, args=(nums, result))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(result)


# Завдання 2

def find_sum(nums, result):
    result['sum'] = sum(nums)

def find_average(nums, result):
    result['average'] = sum(nums) / len(nums)

result = {}

thread1 = threading.Thread(target=find_sum, args=(nums, result))
thread2 = threading.Thread(target=find_average, args=(nums, result))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(result)

# Завдання 3

def save_even(nums, filename= 'even.json'):
    even_nums = [num for num in nums if num % 2 == 0]
    with open(filename, 'w') as file:
        json.dump(even_nums, file)

def save_odd(nums, filename= 'odd.json'):
    odd_nums = [num for num in nums if num % 2 != 0]
    with open(filename, 'w') as file:
        json.dump(odd_nums, file)

def load_even(filename= 'even.json'):
    with open(filename, 'r') as file:
        even_nums = json.load(file)

    print(f"even nums: {even_nums}")

def load_odd(filename= 'odd.json'):
    with open(filename, 'r') as file:
        odd_nums = json.load(file)

    print(f"odd nums: {odd_nums}")


thread1 = threading.Thread(target=save_even, args=(nums,))
thread2 = threading.Thread(target=save_odd, args=(nums,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

load_even()
load_odd()


# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

filename = "search.json"
word = input("Enter a word: ")

def search(word,result):
    with open("search.json", "r") as file:
        items = json.load(file)

    counter = 0

    for item in items:
        if item == word:
            counter += 1

    result[f"amount of word {word}"] = counter

result = {}

thread1 = threading.Thread(target=search,args=('kiwi',result))
thread2 = threading.Thread(target=search,args=('apple',result))
thread3 = threading.Thread(target=search,args=('banana',result))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(result)
