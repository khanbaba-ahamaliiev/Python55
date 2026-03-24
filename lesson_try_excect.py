# Исключения

# try - expect


try:
    num = float(input("Enter a number: "))
    print("number is ", num)
    # код где может быть ошибка

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Please enter a number")

except Exception:  # если случится любая ошибка
    print("помилка")

print("the end")
