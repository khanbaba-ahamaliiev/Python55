countries = {"Usa", "Ukraine", "Germany", "Spain"}

def show():
    for c in sorted(countries, key= lambda s: s.casefold()):
        print(f" - {c}")

def add():
    name = input("enter country name: ")
    countries.add(name)

def remove():
    name = input("enter country name: ")
    countries.remove(name)

def search():
    name = input("enter country name: ")
    matches = [c for c in countries if name in c]
    for c in sorted(matches, key= lambda s: s.casefold()):
        print(f" - {c}")

def check():
    name = input("enter country name: ")
    print("yes "if name in countries else "no")



actions = [add, remove, search, check, show]
while True:
    print("1. add country\n2. remove country\n3. search country\n4. check country\n5. show country")
    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4", "5"]:
        actions[int(choice)-1]()
    else:
        print("invalid choice")





