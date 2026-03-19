def delete_punc(string):
    ls = [",",".", "?", "!", ";", ":"]
    for char in string:
        if char in ls:
            string = string.replace(char, "")
    return string

def sum_vowels(string):

    vowels = "aeiouAEIOU"
    sum_vowels = 0

    for char in string:
        if char in vowels:
            sum_vowels += 1

    return sum_vowels

def palindrome(string):
    string_pal = string.lower().replace(" ", "")
    return string_pal == string_pal[::-1]

if __name__ == '__main__':
    print(delete_punc('wcw.owpo!'))
    print(sum_vowels('wcaw.owpo!'))
    print(palindrome('wca w.oWp o!'))
    print(palindrome('wowow'))





import math


def triangle_Square(a, b, angle):
    radians = math.radians(angle)
    S = 0.5 * (a * b) * math.sin(radians)
    return S

print(triangle_Square(3,4,45))
print(triangle_Square(3,4,90))



import time


def count_time(n=10):
    start = time.time()
    sum_num = 0

    for n in range(1, n+1):
        sum_num += n
    end = time.time()

    return end - start

print(count_time())



import datetime


def count_year(date):
    date = datetime.date.fromisoformat(date)
    today = datetime.date.today()
    age = today - date

    return (age.days) / 365

print(count_year(input("Enter your birth date: ")))



