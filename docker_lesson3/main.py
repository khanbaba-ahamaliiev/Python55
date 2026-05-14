import time
import random
from settings import settings

while True:
    time.sleep(1)
    rand_num = random.randint(
        settings.start_range,
        settings.end_range,
    )
    print(f"random number {rand_num}")
    print(f"secret password {settings.secret_password}")
    print(f"secret login {settings.secret_login}")
