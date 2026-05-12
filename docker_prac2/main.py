from settings import settings
import time


while True:
    time.sleep(1)
    print(settings.filename)
    print(settings.app_name)
    print(settings.login)
    print(settings.password)
    print()
