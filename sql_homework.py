from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import psycopg2
import dotenv
import os

# Для бази даних Академія, яку ви розробили в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє:
# ■ вставляти рядки в таблиці бази даних;
# ■ оновлювати рядків у таблицях бази даних;
# ■ видаляти рядки з таблиць бази даних;


dotenv.load_dotenv()
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DB")

db_url = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()


class AcademyApp:
    def __init__(self):
        self.engine = engine
        self.session = Session()


    def add_row(self, table, **values):
        columns = ", ".join(values.keys())
        params = ", ".join(f":{key}" for key in values.keys())

        query = text(f"""
            INSERT INTO {table} ({columns})
            VALUES ({params})
        """)

        self.session.execute(query, values)
        self.session.commit()


    def update_row(self, table_name, row_id, **values):
        set_clause = ", ".join(
            f"{column} = :{column}"
            for column in values.keys()
        )

        query = text(f"""
            UPDATE {table_name}
            SET {set_clause}
            WHERE Id = :id
        """)

        values["id"] = row_id

        self.session.execute(query, values)
        self.session.commit()

    def delete_row(self, table_name, row_id):
        query = text(f"""
            DELETE FROM {table_name}
            WHERE Id = :id
        """)

        self.session.execute(
            query,
            {"id": row_id}
        )

        self.session.commit()

# ■ створювати звіти:
# ▷ вивести інформацію про всі навчальні групи,

    def show_teachers(self):
        query = text("""
                     SELECT *
                     FROM GROUPS
                     """)

        result = self.session.execute(query)

        for row in result:
            print(row)


# ▷ вивести імена та прізвища викладачів, які читають
# лекції в конкретній групі,


    def show_teachers_by_group(self, group_name):
        query = text("""
                     SELECT DISTINCT T.NAME,
                                     T.SURNAME
                     FROM TEACHERS T
                              JOIN LECTURES L ON T.ID = L.TEACHER_ID
                              JOIN GROUPS_LECTURES GL ON L.ID = GL.LECTURE_ID
                              JOIN GROUPS G ON G.ID = GL.GROUP_ID
                     WHERE G.NAME = :GROUP_NAME
                     """)

        result = self.session.execute(
            query,
            {"GROUP_NAME": group_name}
        )

        for row in result:
            print(f"{row.NAME} {row.SURNAME}")


# ▷ вивести назви предметів, які викладає конкретний
# викладач
    def show_subjects_by_teacher(self, name, surname):
        query = text("""
                     SELECT DISTINCT S.NAME
                     FROM SUBJECTS S
                              JOIN LECTURES L ON S.ID = L.SUBJECT_ID
                              JOIN TEACHERS T ON T.ID = L.TEACHER_ID
                     WHERE T.NAME = :NAME AND T.SURNAME = :SURNAME
                     """)

        result = self.session.execute(
            query,
            {
                "NAME": name,
                "SURNAME": surname
            }
        )

        for row in result:
            print(row.NAME)

# вивести назву предмету, за яким читається найбільше лекцій;

    def show_most_popular_subject(self):
        query = text("""
                     SELECT S.NAME
                     FROM SUBJECTS S
                              JOIN LECTURES L ON S.ID = L.SUBJECT_ID
                     GROUP BY S.ID, S.NAME
                     ORDER BY COUNT(*) DESC
                     LIMIT 1
                     """)

        result = self.session.execute(query)

        for row in result:
            print(row.NAME)

app = AcademyApp


app.add_row(
    "TEACHERS",
    NAME="Ali",
    SURNAME="Mammadov",
    SALARY=2500
)

app.update_row(
    "TEACHERS",
    1,
    SALARY=3000
)

app.delete_row(
    "SUBJECTS",
    5
)

app.show_groups()

app.show_teachers()

app.show_departments()

app.show_teachers_by_group("P107")

app.show_subjects_by_teacher(
    "Ali",
    "Mammadov"
)

app.show_most_popular_subject()
