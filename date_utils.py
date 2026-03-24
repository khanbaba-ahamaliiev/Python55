# Завдання 1
import datetime
import math
import time


def water_colder_time(T_env, T0, t, k=0.03):
    return T_env + (T0 - T_env) * math.exp(-k * t)


fridge_temp = 18
water_temp = 40
colder_time = 100

print(water_colder_time(fridge_temp, water_temp, colder_time))


# Завдання 2


def get_func_time(show_time: bool):
    start_time = time.time()

    ask_name = input("what is your name? ")

    end_time = time.time()

    if show_time == True:
        print(f"час роботи функції складає: {end_time - start_time}")

    return ask_name


get_func_time(True)

# Завдання 3


def days_left_deadline(deadline):
    deadline = datetime.date.fromisoformat(deadline)

    today = datetime.date.today()
    left_days = deadline - today
    if left_days < datetime.timedelta(days=7):
        print("залишилось меньше тижня до дедлайну")
    return (left_days).days


deadline_date = input("enter deadline (format: YYYY-MM-DD): ")

if __name__ == "__main__":
    days_left_deadline(deadline_date)
