# базовый образ с Python 3.14
# Версия пайтона
FROM python:3.14-slim

#базовая директория
WORKDIR app

#копируем все файлы из текущей директории в контейнер
COPY ./ ./

# встановлення бібліотек
RUN pip install -r requirements.txt

# відкрити порт
EXPOSE 8080

#команда для запуска
CMD ["python", "main.py"]
