-- Завдання 1
-- Створіть базу даних Академія (Academy), яка міститиме
-- інформацію про співробітників та внутрішній порядок академії.
-- Опис бази даних знаходиться в кінці файлу.

-- CREATE DATABASE ACADEMY

-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE DEPARTMENTS (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	FINANCING MONEY NOT NULL DEFAULT 0 CHECK (FINANCING >= 0::MONEY),
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (FINANCING, NAME) VALUES
-- (250000.00, 'Department of Computer Science'),
-- (180000.00, 'Department of Mathematics'),
-- (150000.00, 'Department of Applied Physics'),
-- (120000.00, 'Department of Information Security'),
-- (195000.00, 'Department of Artificial Intelligence'),
-- (110000.00, 'Department of Software Engineering'),
-- (85000.00,  'Department of Data Science'),
-- (135000.00, 'Department of Systems Analysis'),
-- (90000.00,  'Department of Web Technologies'),
-- (105000.00, 'Department of Robotics and Automation');


-- ¾ Факультети(Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Декан (Dean). Декан факультету.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнім.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE FACULTIES (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	DEAN VARCHAR(255) NOT NULL,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO FACULTIES (DEAN, NAME) VALUES
-- ('Dr. Alan Turing', 'Faculty of Computer Science and Engineering'),
-- ('Dr. Emmy Noether', 'Faculty of Mathematics and Statistics'),
-- ('Dr. Marie Curie', 'Faculty of Physics and Astronomy'),
-- ('Dr. Ada Lovelace', 'Faculty of Information Technology'),
-- ('Dr. Richard Feynman', 'Faculty of Natural Sciences'),
-- ('Dr. Grace Hopper', 'Faculty of Software Development'),
-- ('Dr. Claude Shannon', 'Faculty of Cybernetics'),
-- ('Dr. Katherine Johnson', 'Faculty of Aerospace Engineering'),
-- ('Dr. Tim Berners-Lee', 'Faculty of Digital Media and Design'),
-- ('Dr. Nikola Tesla', 'Faculty of Electrical Engineering');

-- ¾ Групи (Groups)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва групи.
-- ▷ Тип даних — varchar(10).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Рейтинг (Rating). Рейтинг групи.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 0 до 5.
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.

-- CREATE TABLE GROUPS (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	NAME VARCHAR(10) NOT NULL UNIQUE,
-- 	RATING INT NOT NULL CHECK(RATING BETWEEN 0 AND 5),
-- 	YEAR INT NOT NULL CHECK(YEAR BETWEEN 1 AND 5)
-- )

-- INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
-- ('CS-101', 4, 1),
-- ('CS-102', 3, 1),
-- ('MA-201', 5, 2),
-- ('MA-202', 4, 2),
-- ('PH-301', 2, 3),
-- ('IT-302', 5, 3),
-- ('SE-401', 4, 4),
-- ('SE-402', 3, 4),
-- ('DS-501', 5, 5),
-- ('AI-103', 4, 1),
-- ('CY-203', 3, 2),
-- ('AE-303', 5, 3),
-- ('EE-403', 2, 4),
-- ('RO-502', 4, 5),
-- ('ST-104', 3, 1);

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Дата працевлаштування (EmploymentDate). Дата працевлаштування викладача.
-- ▷ Тип даних — date.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше 01.01.1990.
-- ■ Асистент (IsAssistant). Чи є викладач асистентом.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Професор (IsProfessor). Чи є викладач професором.
-- ▷ Тип даних — bit.
-- ▷ Не містить null-значення.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — nvarchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Посада (Position). Посада викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Надбавка (Premium). Надбавка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — money.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE TEACHERS (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	EMPLOYMENT_DATE DATE NOT NULL CHECK(EMPLOYMENT_DATE >= '1990-01-01'),
-- 	is_assistant BOOLEAN DEFAULT FALSE NOT NULL,
-- 	IS_PROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
-- 	NAME TEXT NOT NULL,
-- 	POSITION TEXT NOT NULL,
-- 	PREMIUM MONEY NOT NULL CHECK(PREMIUM >= 0::MONEY) DEFAULT 0,
-- 	SALARY MONEY NOT NULL CHECK(SALARY >= 0::MONEY),
-- 	SURNAME TEXT NOT NULL
-- )

-- INSERT INTO TEACHERS (EMPLOYMENT_DATE, is_assistant, IS_PROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME) VALUES
-- ('1995-09-01', FALSE, TRUE,  'James',     'Professor & Chair',   550.00,  4500.00, 'Smith'),
-- ('2002-02-15', FALSE, TRUE,  'Patricia',  'Professor',           400.00,  4100.00, 'Johnson'),
-- ('2010-09-01', FALSE, FALSE, 'Robert',    'Associate Professor', 250.00,  3500.00, 'Williams'),
-- ('2015-03-01', FALSE, FALSE, 'Jennifer',  'Assistant Professor', 150.00,  3100.00, 'Brown'),
-- ('2020-09-01', TRUE,  FALSE, 'Michael',   'Junior Lecturer',       0.00,  2200.00, 'Jones'),
-- ('1990-01-05', FALSE, TRUE,  'Elizabeth', 'Senior Professor',    600.00,  4800.00, 'Garcia'),
-- ('2005-11-10', FALSE, FALSE, 'David',     'Associate Professor', 300.00,  3600.00, 'Miller'),
-- ('2018-09-01', TRUE,  FALSE, 'Barbara',   'Teaching Assistant',   50.00,  2100.00, 'Davis'),
-- ('2012-04-01', FALSE, FALSE, 'William',   'Senior Lecturer',     200.00,  3300.00, 'Rodriguez'),
-- ('2022-01-10', TRUE,  FALSE, 'Susan',     'Lab Instructor',        0.00,  1950.00, 'Martinez'),
-- ('1998-09-01', FALSE, TRUE,  'Richard',   'Professor',           450.00,  4300.00, 'Hernandez'),
-- ('2008-07-20', FALSE, FALSE, 'Jessica',   'Associate Professor', 280.00,  3550.00, 'Lopez'),
-- ('2016-09-01', FALSE, FALSE, 'Thomas',    'Assistant Professor', 120.00,  3050.00, 'Gonzalez'),
-- ('2021-02-28', TRUE,  FALSE, 'Sarah',     'Teaching Assistant',    0.00,  2000.00, 'Wilson'),
-- ('2000-03-15', FALSE, TRUE,  'Charles',   'Professor',           500.00,  4400.00, 'Anderson'),
-- ('2014-09-01', FALSE, FALSE, 'Karen',     'Senior Lecturer',     180.00,  3250.00, 'Thomas'),
-- ('2019-05-12', TRUE,  FALSE, 'Christopher','Lecturer',            80.00,  2400.00, 'Taylor'),
-- ('1993-10-01', FALSE, TRUE,  'Nancy',     'Professor',           520.00,  4600.00, 'Moore'),
-- ('2011-01-15', FALSE, FALSE, 'Matthew',   'Associate Professor', 270.00,  3650.00, 'Jackson'),
-- ('2023-09-01', TRUE,  FALSE, 'Lisa',      'Junior Assistant',      0.00,  1900.00, 'Martin');


-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.

-- SELECT *
-- FROM DEPARTMENTS
-- ORDER BY ID DESC

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.

-- SELECT NAME, RATING
-- FROM GROUPS

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).

-- SELECT SURNAME, (PREMIUM / SALARY) * 100 AS PERSENT
-- FROM TEACHERS

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».

-- SELECT 'The dean of faculty ' || NAME || ' is ' || DEAN || '.' AS FACULTY
-- FROM FACULTIES

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.

-- SELECT SURNAME
-- FROM TEACHERS
-- WHERE SALARY > 1050::MONEY

-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 25000.

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE FINANCING <= 11000::MONEY OR FINANCING >= 25000::MONEY

-- 7. Вивести назви факультетів, окрім факультету «Computer
-- Science».

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE NAME <> 'Department of Computer Science'

-- 8. Вивести прізвища та посади викладачів, які не є професорами

-- SELECT SURNAME, POSITION
-- FROM TEACHERS
-- WHERE IS_PROFESSOR = FALSE
