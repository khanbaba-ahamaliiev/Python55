from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import psycopg2
import dotenv
import os

# Параметры подключение к базе данных

# host = "localhost"
# port = 5432
# user = "postgres"
# password = "hanik2004"
# db = "people"

#  лучше это в .env сохранять

# читаем из .env
dotenv.load_dotenv()
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DB")

# путь до базы данных
db_url = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"


# создание подключения(engine)
engine = create_engine(db_url)


# создание сессии(session) на основе движка
Session = sessionmaker(bind=engine)#класс с возможностью подключения к базеданных
session = Session()


# получение данных мз базы данных

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))

# запуск sql запросы
student_name = input("Enter student name: ")
query = f"""
    SELECT *
    FROM STUDENTS
    WHERE name = '{student_name}'
"""

# ПОДПРАВИТЬ ТЕКСТ
query = text(query)

# получение результата
result = session.execute(query)

for row in result:
    print(row)
