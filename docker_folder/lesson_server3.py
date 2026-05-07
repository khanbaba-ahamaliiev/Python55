import time
import random

while True:
    time.sleep(1)
    print(random.randint(1,100))

# создание образа
# docker build -t [name] [путь до докер файла]

# запуск контейнера
# docker run (-d) --name [container_name] [image_name]
