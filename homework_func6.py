# Завдання 1

func1 = lambda n : n * -1
print(func1(5))

func2 = lambda s : s != ""
print(func2("hello"))
print(func2(""))

# Завдання 2

def average_filter(nums):
    average = sum(nums) / len(nums)

    return list(filter(lambda n: n > average, nums))

print(average_filter([1,2,3,4,5]))


def word_filter(words):
    return list(filter(lambda n: len(n) == 4, words))

print(word_filter(['car', 'john', 'kiev', 'skyscraper']))


# Завдання 3

def letter_counter(words, letter):
    goal = ""

    for word in words:
        if word.count(letter) > goal.count(letter):
            goal = word

    return goal

print(letter_counter(['car', 'apple', "banana", "sky"], 'a'))