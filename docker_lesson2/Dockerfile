# версия пайтона
FROM python:3.11-slim

# базовая папка
WORKDIR /app

# скопировать все файлы в папку
COPY ./ ./

RUN pip install -r requirements.txt
# указать настройки (переменные окружения)
ENV MIN_NUM=0

# команда для запуска
CMD ["python", "-u", "main.py"]
