class CreditCardPayment:
    def __init__(self, currency:str):
        self._currency = currency

    def pay(self, amount:int):
        print(f'оплата карткою {amount} {self._currency}')


class PayPalPayment:
    def __init__(self, currency:str):
        self._currency = currency

    def pay(self, amount:int):
        print(f'оплата PayPal {amount} {self._currency}')


class CryptoPayment:
    def __init__(self, currency:str):
        self._currency = currency

    def pay(self, amount:int):
        print(f'оплата криптогаманцем {amount} {self._currency}')


def create_payment()->PayPalPayment | CryptoPayment | CreditCardPayment | None:
    payment = input("Введіть тип рахунку(CreditCard, PayPal, CryptoPayment): ")

    if payment == 'CreditCard':
        currency = input('Введіть валюту ')
        return CreditCardPayment(currency)

    elif payment == 'PayPal':
        currency = input('Введіть валюту ')
        return PayPalPayment(currency)

    elif payment == 'CryptoPayment':
        currency = input('Введіть валюту ')
        return CryptoPayment(currency)

    else:
        print("invalid input")
        return None

payments = []

for _ in range(3):
    payments.append(create_payment())

for payment in payments:
    if payment is None:
        print("payment not in the mood")
        continue

    amount = int(input("введіть кількість "))
    if amount <= 0:
        print("неправильна сума")
        continue

    payment.pay(amount)
