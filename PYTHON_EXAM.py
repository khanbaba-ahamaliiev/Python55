import datetime


# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 > num2:
    num1, num2 = num2, num1

sum_range = 0

for n in range(num1, num2+1): # з самими числами включно
    sum_range += n

print(f"sum in range {num1} and {num2} is {sum_range}")

# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.
sum_between = 0

for n in range(1,100+1): # 100+1 для наглядності, бо stop не включає саме число
    if n % 2 == 0:
        sum_between += n

print(f"sum of even numbers between 1 to 100 is {sum_between}")

# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.
sentence = input("enter your sentence: ")

for l in sentence:
    if l == " ": # - якщо пробіл не важається літерою
        continue

    print(l)


# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.
# ls = list(map(int, input("enter number for list by space: ").split()))
ls = [7, 4, 2, 8, 1, 9, 5, 6]

new_list = []
for n in ls:
    if n % 2 == 0:
        new_list.append(n)

print(f"new list: {new_list}")

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

def upper_checker(ls:list):
    new_sentences = []
    for sentence in ls:
        if sentence[0].isupper():
            new_sentences.append(sentence)

    print(f"new list of sentences: {new_sentences}")
    return new_sentences

sentences = ["Kyiv", "how are you", "Apple", "friend"]
upper_checker(sentences)

# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
def python_checker(ls:list):
    new_list = []
    for sentence in ls:
        if "python" in sentence.lower():
            new_list.append(sentence)

    print(f"new list of sentences with python: {new_list}")
    return new_list

sentences = ["python", "I like Python", "java", "c++"]
python_checker(sentences)

# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.
dictionary = {}

while True:
    print("1 - find definition")
    print("2 - add new word")
    print("3 - remove a word")
    print("4 - show all words")
    print("5 - exit")

    user_choice = input("select option(1-5): ")

    if not user_choice.isdigit():
        print("not such option. try again")
        continue

    if int(user_choice) < 1 or int(user_choice) > 5:
        print("not such option. try again")
        continue

    if user_choice == "1":
        word = input("enter your word")

        if word in dictionary:
            print(f"{word} - {dictionary[word]}")
        else:
            print(f" {word} not found")

    elif user_choice == "2":
        word = input("add new word ")
        if word in dictionary:
            print(f"{word} already exists")
            continue
        definition = input(f"enter definition for {word}: ")
        if definition:
            dictionary[word] = definition
            print(f"definition added for {word}")
        else:
            print("definition cant be empty")

    elif user_choice == "3":
        word = input("enter your word")

        if word in dictionary:
            del dictionary[word]
            print(f"{word} removed")
        else:
            print(f"{word} not found")

    elif user_choice == "4":
        if dictionary:
            print("all words")
            for word, definition in dictionary.items():
                print(f"{word} — {definition}")
        else:
            print("dictionary empty")

    elif user_choice == "5":
        print("good bye")
        break


# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).
cort = [(1, 3), (3, 2), (2, 1)]

sorted_cort = sorted(cort, key=lambda x: x[1])

print(sorted_cort)

# Частина 2: Об'єктно-орієнтоване програмування (ООП)
# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
class WebSite:
    def __init__(self, url:str, name:str):
        self.url = url
        self.name = name
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)
        print(f"{page.title} added")



    def remove_page(self, page_name):
        found = False
        for page in self.pages:
            if page.title == page_name:
                self.pages.remove(page)
                print(f"{page.title} removed")
                found = True
                break

        if not found:
            print("page not found")


    def show_info(self):
        print(f"site name: {self.name}")
        print(f"URL: {self.url}")

        if not self.pages:
            print("pages not found")
            return

        print("pages:")
        for page in self.pages:
            print(f"- {page.title}")

# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
class WebPage:
    def __init__(self, title, content, date_publish):
        self.title = title
        self.content = content
        self.date_publish = date_publish

    def show_info(self):
        print(f"title: {self.title}")
        print(f"content: {self.content}")
        print(f"date: {self.date_publish}")


# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.




def main():
    my_site = None

    while True:
        print("1 - create site(or recreate)")
        print("2 - add new page")
        print("3 - remove page")
        print("4 - show all pages")
        print("5 - show page by title")
        print("6 - exit")

        user_choice = input("select option(1-5): ")

        if not user_choice.isdigit():
            print("not such option. try again")
            continue

        if int(user_choice) < 1 or int(user_choice) > 5:
            print("not such option. try again")
            continue

        if user_choice == "1":
            name = input("enter a sites name: ")
            url = input("enter a sites url: ")

            if not name:
                print("site name cannot be empty")
                continue

            if not url:
                print("url cannot be empty")
                continue

            my_site = WebSite(url, name)
            print("site created")

        elif user_choice == "2":
            if not my_site:
                print("site not found. please create it")
                continue

            title = input("enter a page title: ")
            content = input("enter a page content: ")

            if not title:
                print("title cannot be empty")
                continue

            if not content:
                print("content cannot be empty")
                continue

            date_publish = datetime.datetime.now()

            new_page = WebPage(title, content, date_publish)
            my_site.add_page(new_page)

        elif user_choice == "3":
            if not my_site:
                print("site not found. please create it")
                continue

            if not my_site.pages:
                print("pages not found. create it")
                continue

            title_remove = input("enter a title for remove page: ")
            my_site.remove_page(title_remove)

        elif user_choice == "4":
            if not my_site:
                print("site not found. please create it")
                continue

            my_site.show_info()

        elif user_choice == "5":

            if not my_site:
                print("site not found. please create it")

                continue

            title = input("enter page title: ")

            for page in my_site.pages:
                if page.title == title:
                    page.show_info()

        elif user_choice == "6":
            print("thanks for using our system. you exit")
            break

if __name__ == '__main__':
    main()
