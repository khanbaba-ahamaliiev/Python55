# # КОРТЕЖ - tuple() - неизменный тип данных
#
# # функция map - применяет <func> к каждому элементу последовательности
#
# user_data = input("enter numbers separated by a comma")
# nums = user_data.split(", ")
# print(nums)
#
# new_nums = list(map(int, nums))
# print(new_nums)
#

# КОРТЕЖ

nums = (1, 2, 3, 4)

def get_statistic():
    count = 5
    average = 10.5

    return count, average # - возвращает кортеж

# enumerate

words = ['apple', 'banana', 'orange', 'pear', 'cherry']

for i in range (len(words)):
    word = words[i]

    print(i, word)

for i, word in enumerate(words, start=1): # - одно и тоже с тем что сверху
    print(i, word)


item = ['bread', 'milk', 'cheese']
prices = [30, 70, 150]

for pair in zip(item, prices):
    print(pair)

















