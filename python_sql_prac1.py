from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import sessionmaker
import psycopg2
import dotenv
import os


# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє створювати звіти:

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

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))


# ▷ Вивести прізвища лікарів та їх спеціалізації;

def show_doctors_specializations(session):
    query = f"""
        SELECT D.SURNAME, S.NAME
        FROM DoctorsSpecializations DS
            JOIN DOCTORS D ON DS.DOCTOR_ID = D.ID
            JOIN SPECIALIZATIONS S ON DS.SPECIALIZATION_ID = S.ID

    """
    query = text(query)

    result = session.execute(query)
    print("\t--doctors surname and specialization--")
    for row in result:
        print(row)


# show_doctors_specializations(session)

# Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які перебувають у відпустці;

def show_doctors_salary(session):
    query = """
        SELECT D.SURNAME, D.SALARY + D.PREMIUM
        FROM DOCTORS D JOIN VACATIONS V ON D.ID = V.DOCTOR_ID
        WHERE V.ENDDATE > CURRENT_DATE AND V.STARTDATE < CURRENT_DATE

    """

    query = text(query)

    result = session.execute(query)

    print("\t--doctors surname and salary--")
    for row in result:
        print(row)

# show_doctors_salary(session)


# ▷ Вивести назви палат, які знаходяться у певному відділенні;

def show_dep_names(session):
    query = """
        SELECT NAME
        FROM DEPARTMENTS;
    """
    query = text(query)

    result = session.execute(query)

    print("\t--names departments--")

    for row in result:
        print(row)

def show_wards(session):
    show_dep_names(session)

    department_name = input("enter department name: ")

    query = f"""
        SELECT *
        FROM WARDS W
            JOIN DEPARTMENTS D ON D.ID = W.DEPARTMENT_ID
        WHERE D.NAME = '{department_name}'

    """
    query = text(query)

    result = session.execute(query)

    print("\t--wards names and departments--")
    for row in result:
        print(row)


# show_wards(session)



# ▷ Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;

def show_donation(session):

    month_num = input("enter month number ")
    year_num = input("enter  year number ")
    query = f"""
        SELECT DEP.NAME, S.NAME, D.AMOUNT, D.DONATION_DATE
        FROM DONATIONS D
            JOIN DEPARTMENTS DEP ON D.DEPARTMENT_ID = DEP.ID
            JOIN SPONSORS S ON D.SPONSOR_ID = S.ID
        WHERE EXTRACT(MONTH FROM D.DONATION_DATE) = '{month_num}' AND EXTRACT(YEAR FROM D.DONATION_DATE) = '{year_num}'
    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)


show_donation(session)

# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.
