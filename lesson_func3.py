import time

l1 = lambda n: n**2
l2 = lambda a, b, c: a + b + c
l3 = lambda surname, name: f'"{surname}, {name}"'
l4 = lambda n: n % 2 == 0


ls = [-2, 1, 0, -5, 12]
fl1 = list(filter(lambda n: n > 0, ls))
print(fl1)


ls = ["car", "dog", "string", "city", "lambda"]
fl2 = list(filter(lambda word: len(word) > 3, ls))
print(fl2)


def filter_by_letter(words, letter):
    return list(filter(lambda word: word.lower().startswith(letter.lower()), words))


ls = ["car", "dog", "string", "city", "lambda"]
letter = "c"

print(filter_by_letter(ls, letter))


def time_func(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start


def count_to_n(n):
    for num in range(1, n + 1):
        print(num)


print(time_func(count_to_n, 5))


def sort_by_last_letter(ls):
    return sorted(ls, key=lambda word: word[-1])


print(sort_by_last_letter(ls))


def sort_by_amount_numbers(ls):
    return sorted(ls, key=lambda number: len(str(number)))


nums = [5, 123, 45, 9, 1000, 12]
print(sort_by_amount_numbers(nums))


def shortest_word(ls):
    return min(ls, key=len)


print(shortest_word(ls))
