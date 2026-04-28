import random
import json


def start_game():
    global result

    for _ in range(5):
        guess = int(input("Guess a number: "))
        answers.append(guess)

        if answers[_] == secret:
            result = 'win'
            print("You won!")
            break

    if secret not in answers:
        result = 'lose'
        print("You lost!")

def generate_secret():
    return random.randint(1,100)

def show_results(games_history):
    win_score = 0
    lose_score = 0
    for game in games_history:
        if game["result"] == 'win':
            win_score += 1
        if game["result"] == 'lose':
            lose_score += 1

    print(f"win: {win_score}, lose: {lose_score}")

def save_data(data):
    games_history.append(data)

    with open("game.json", "w", encoding='utf-8') as file:
        json.dump(games_history, file, indent=4, ensure_ascii=False)

def load_data(data):
    global games_history

    try:
        with open("game.json", "r", encoding='utf-8') as file:
            games_history = json.load(file)

    except FileNotFoundError:
        games_history = []

def end_screen():
    print(f'secret number was {secret}')

def main():
    global secret, answers

    secret = generate_secret()
    answers = []

    start_game()
    end_screen()

    data = {
        'secret': secret,
        'answers': answers,
        'result': result,
    }

    load_data(data)
    save_data(data)

    show_results(games_history)


if __name__ == '__main__':
    main()
