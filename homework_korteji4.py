# Завдання 1
currencies = {"UAH": 1, "USD": 41.2, "EUR": 44.5, "PLN": 10.3, "GBP": 52.0}

while True:
    currency1 = input("введіть назву валюти(UAH, USD, EUR, PLN, GBP): ")
    if currency1 == "":
        break

    if currency1 not in currencies:
        print("Не правильно введена валюта")
        continue

    amount_currency1 = float(input("введіть кількість валюти: "))
    if amount_currency1 <= 0:
        print("Не правильно введена кількість валюти")
        continue

    currency2 = input("введіть назву нової валюти: ")
    if currency1 not in currencies:
        print("Не правильно введена валюта")
        continue

    uah = currencies[currency1] * amount_currency1
    exchange = uah / currencies[currency2]

    print(f"{amount_currency1} {currency1} робить {exchange} {currency2}")

# Завдання 2


def workers(in_office, out_office):
    in_office = set(in_office)
    out_office = set(out_office)

    all_workers = in_office | out_office
    print(f"Імена усіх працівників: \n{all_workers}")

    in_out_office = in_office & out_office
    print(f"Імена працівників, які працюють і в офісі, і віддалено: \n{in_out_office}")

    in_out_rate = len(in_out_office) / len(all_workers)
    print(
        f"Відсоток працівників, які працюють і в офісі, і віддалено: {in_out_rate:.1%}"
    )


office_workers = {"anna", "ivan", "olga", "maksym", "iryna", "dmytro", "taras"}

remote_workers = {"olga", "maksym", "iryna", "andrii", "sofia", "taras", "nazar"}

if __name__ == "__main__":
    workers(office_workers, remote_workers)
