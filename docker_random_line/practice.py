import random
from settings import settings
import time

while True:
    time.sleep(settings.delay)

    randon_len = random.randint(settings.min_len, settings.max_len)
    print(settings.symbol * randon_len)
