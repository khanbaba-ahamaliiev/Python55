-- Таблиці
-- Нижче наведено детальний опис структури кожної
-- таблиці.
-- ¾ Куратори (Curators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Прізвище (Surname). Прізвище куратора.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE CURATORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(200) NOT NULL,
-- 	SURNAME VARCHAR(200) NOT NULL
-- )

-- INSERT INTO CURATORS (NAME, SURNAME) VALUES
-- ('John', 'Smith'),
-- ('Jane', 'Doe'),
-- ('Michael', 'Johnson'),
-- ('Emily', 'Williams'),
-- ('David', 'Brown'),
-- ('Sarah', 'Jones'),
-- ('James', 'Garcia'),
-- ('Jessica', 'Miller'),
-- ('Robert', 'Davis'),
-- ('Ashley', 'Rodriguez'),
-- ('William', 'Martinez'),
-- ('Amanda', 'Hernandez'),
-- ('Brian', 'Lopez'),
-- ('Megan', 'Gonzalez'),
-- ('Kevin', 'Wilson'),
-- ('Rachel', 'Anderson'),
-- ('Thomas', 'Thomas'),
-- ('Christine', 'Taylor'),
-- ('Steven', 'Moore'),
-- ('Katherine', 'Jackson'),
-- ('Andrew', 'Martin'),
-- ('Stephanie', 'Lee'),
-- ('Joshua', 'Perez'),
-- ('Laura', 'Thompson'),
-- ('Daniel', 'White'),
-- ('Julie', 'Harris'),
-- ('Christopher', 'Sanchez'),
-- ('Rebecca', 'Clark'),
-- ('Matthew', 'Ramirez'),
-- ('Mathew', 'Lewis');


-- ¾ Кафедри (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування кафедри.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва кафедри.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ідентифікатор факультету (FacultyId). Факультет, до складу
-- якого належить кафедра.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE DEPARTMENTS (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	FINANCING DECIMAL(10, 2) NOT NULL CHECK (FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	FACULTY_ID INT NOT NULL,
-- 	FOREIGN KEY (FACULTY_ID) REFERENCES FACULTIES(ID)
-- )

-- INSERT INTO DEPARTMENTS (FINANCING, NAME, FACULTY_ID) VALUES
-- (45000.00, 'Department of Artificial Intelligence', 1),
-- (35000.00, 'Department of Mathematical Analysis', 2),
-- (28000.50, 'Department of Organic Chemistry', 3),
-- (30000.00, 'Department of Genetics and Cell Biology', 4),
-- (75000.00, 'Department of Cardiology and Surgery', 5),
-- (15000.00, 'Department of Ancient History', 6),
-- (12000.00, 'Department of Ethics and Logic', 7),
-- (22000.00, 'Department of Macroeconomics', 8),
-- (25000.75, 'Department of Criminal Law', 9),
-- (50000.00, 'Department of Robotics and Automation', 10),
-- (18000.00, 'Department of Social Psychology', 11),
-- (21000.00, 'Department of Clinical Psychology', 12),
-- (14000.00, 'Department of Applied Linguistics', 13),
-- (32000.00, 'Department of Strategic Management', 14),
-- (40000.00, 'Department of Urban Planning and Design', 15),
-- (16000.00, 'Department of Digital Journalism', 16),
-- (27000.00, 'Department of Ecology and Climate Change', 17),
-- (19000.00, 'Department of International Relations', 18),
-- (11000.00, 'Department of Classical Painting', 19),
-- (0.00, 'Department of Comparative Theology', 20);


-- ¾ Факультети (Faculties)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- факультету.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Фінансування (Financing). Фонд фінансування факультету.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва факультету.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE FACULTIES(
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	FINANCING DECIMAL(10, 2) NOT NULL CHECK (FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO FACULTIES (FINANCING, NAME) VALUES
-- (250000.00, 'Faculty of Computer Science'),
-- (180000.50, 'Faculty of Mathematics and Physics'),
-- (150000.00, 'Faculty of Chemistry'),
-- (135000.00, 'Faculty of Biology'),
-- (310000.00, 'Faculty of Medicine and Health Sciences'),
-- (95000.00, 'Faculty of History'),
-- (85000.00, 'Faculty of Philosophy'),
-- (110000.00, 'Faculty of Economics'),
-- (125000.75, 'Faculty of Law'),
-- (140000.00, 'Faculty of Engineering and Technology'),
-- (90000.00, 'Faculty of Sociology'),
-- (105000.00, 'Faculty of Psychology'),
-- (75000.00, 'Faculty of Philology and Linguistics'),
-- (115000.00, 'Faculty of Business Administration'),
-- (165000.00, 'Faculty of Architecture and Design'),
-- (80000.00, 'Faculty of Journalism and Media'),
-- (130000.00, 'Faculty of Environmental Sciences'),
-- (95000.00, 'Faculty of Political Science'),
-- (60000.00, 'Faculty of Fine Arts'),
-- (0.00, 'Faculty of Theology');


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
-- ■ Курс (Year). Курс (рік), на якому навчається група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Ідентифікатор кафедри (DepartmentId). Кафедра, до складу
-- якої належить група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS (
-- 	ID SERIAL PRIMARY KEY NOT NULL,
-- 	NAME VARCHAR(10) NOT NULL UNIQUE,
-- 	YEAR INT NOT NULL CHECK (1 <= YEAR AND YEAR <= 5),
-- 	DEPARTMENT_ID INT NOT NULL,
-- 	FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(ID)
-- )

-- INSERT INTO GROUPS (NAME, YEAR, DEPARTMENT_ID) VALUES
-- -- Кафедра 1: Artificial Intelligence
-- ('AI-101', 1, 1), ('AI-302', 3, 1),
-- -- Кафедра 2: Mathematical Analysis
-- ('MA-201', 2, 2), ('MA-402', 4, 2),
-- -- Кафедра 3: Organic Chemistry
-- ('OC-101', 1, 3), ('OC-502', 5, 3),
-- -- Кафедра 4: Genetics and Cell Biology
-- ('GC-301', 3, 4), ('GC-402', 4, 4),
-- -- Кафедра 5: Cardiology and Surgery
-- ('CS-201', 2, 5), ('CS-502', 5, 5),
-- -- Кафедра 6: Ancient History
-- ('AH-101', 1, 6), ('AH-202', 2, 6),
-- -- Кафедра 7: Ethics and Logic
-- ('EL-301', 3, 7), ('EL-402', 4, 7),
-- -- Кафедра 8: Macroeconomics
-- ('ME-101', 1, 8), ('ME-502', 5, 8),
-- -- Кафедра 9: Criminal Law
-- ('CL-201', 2, 9), ('CL-302', 3, 9),
-- -- Кафедра 10: Robotics and Automation
-- ('RA-401', 4, 10), ('RA-502', 5, 10),
-- -- Кафедра 11: Social Psychology
-- ('SP-101', 1, 11), ('SP-202', 2, 11),
-- -- Кафедра 12: Clinical Psychology
-- ('CP-301', 3, 12), ('CP-402', 4, 12),
-- -- Кафедра 13: Applied Linguistics
-- ('AL-101', 1, 13), ('AL-502', 5, 13),
-- -- Кафедра 14: Strategic Management
-- ('SM-201', 2, 14), ('SM-302', 3, 14),
-- -- Кафедра 15: Urban Planning and Design
-- ('UP-401', 4, 15), ('UP-502', 5, 15),
-- -- Кафедра 16: Digital Journalism
-- ('DJ-101', 1, 16), ('DJ-202', 2, 16),
-- -- Кафедра 17: Ecology and Climate Change
-- ('EC-301', 3, 17), ('EC-402', 4, 17),
-- -- Кафедра 18: International Relations
-- ('IR-101', 1, 18), ('IR-502', 5, 18),
-- -- Кафедра 19: Classical Painting
-- ('CP-201', 2, 19), ('CP-302', 3, 19),
-- -- Кафедра 20: Comparative Theology
-- ('CT-401', 4, 20), ('CT-502', 5, 20);

-- ¾ Групи та куратори (GroupsCurators)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- куратора.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор куратора (CuratorId). Куратор.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS_CURATORS (
--     ID SERIAL PRIMARY KEY NOT NULL,
--     CURATOR_ID INT NOT NULL,
--     GROUP_ID INT NOT NULL,
--     FOREIGN KEY (CURATOR_ID) REFERENCES CURATORS(ID),
--     FOREIGN KEY (GROUP_ID) REFERENCES GROUPS(ID)
-- )

-- INSERT INTO GROUPS_CURATORS (CURATOR_ID, GROUP_ID) VALUES
-- (1, 10), (2, 9),  (3, 8),  (4, 7),  (5, 6),
-- (6, 5),  (7, 4),  (8, 3),  (9, 2),  (10, 1),
-- (11, 40), (12, 39), (13, 38), (14, 37), (15, 36),
-- (16, 35), (17, 34), (18, 33), (19, 32), (20, 31),
-- (21, 11), (22, 12), (23, 13), (24, 14), (25, 15),
-- (26, 16), (27, 17), (28, 18), (29, 19), (30, 20);

-- ¾ Групи та лекції (GroupsLectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
-- лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ідентифікатор групи (GroupId). Група.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор лекції (LectureId). Лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.

-- CREATE TABLE GROUPS_LECTURES (
--     ID SERIAL PRIMARY KEY NOT NULL,
--     GROUP_ID INT NOT NULL,
--     LECTURE_ID INT NOT NULL,
--     FOREIGN KEY (GROUP_ID) REFERENCES GROUPS(ID),
--     FOREIGN KEY (LECTURE_ID) REFERENCES LECTURES(ID)
-- );

-- INSERT INTO GROUPS_LECTURES (GROUP_ID, LECTURE_ID) VALUES
-- (1, 1),   (2, 2),   (3, 3),   (4, 4),   (5, 5),
-- (6, 6),   (7, 7),   (8, 8),   (9, 9),   (10, 10),
-- (11, 11), (12, 12), (13, 13), (14, 14), (15, 15),
-- (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
-- (21, 21), (22, 22), (23, 23), (24, 24), (25, 25),
-- (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
-- (31, 1),  (32, 2),  (33, 3),  (34, 4),  (35, 5),
-- (36, 6),  (37, 7),  (38, 8),  (39, 9),  (40, 10);


-- ¾ Лекції (Lectures)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор лекції.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Аудиторія (LectureRoom). Аудиторія, в якій проходить
-- лекція.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Ідентифікатор предмета (SubjectId). Предмет, з якого читається лекція.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.
-- ■ Ідентифікатор викладача (TeacherId). Викладач, який веде
-- лекцію.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Зовнішній ключ.


-- CREATE TABLE LECTURES (
--     ID SERIAL PRIMARY KEY NOT NULL,
--     LECTURE_ROOM TEXT NOT NULL CHECK (LECTURE_ROOM <> ''),
--     SUBJECT_ID INT NOT NULL,
--     TEACHER_ID INT NOT NULL,
--     FOREIGN KEY (SUBJECT_ID) REFERENCES SUBJECTS(ID),
--     FOREIGN KEY (TEACHER_ID) REFERENCES TEACHERS(ID)
-- )

-- INSERT INTO LECTURES (LECTURE_ROOM, SUBJECT_ID, TEACHER_ID) VALUES
-- ('Room 101', 1, 1),   ('Auditorium A', 2, 2),  ('Room 305', 3, 3),
-- ('Lab 2', 4, 4),       ('Room 402', 5, 5),      ('Auditorium B', 6, 6),
-- ('Room 204', 7, 7),   ('Room 105', 8, 8),      ('Room 312', 9, 9),
-- ('Lab 5', 10, 10),    ('Room 102', 11, 11),    ('Auditorium C', 12, 12),
-- ('Room 306', 13, 13),  ('Lab 3', 14, 14),      ('Room 403', 15, 15),
-- ('Auditorium D', 16, 16), ('Room 205', 17, 17),  ('Room 106', 18, 18),
-- ('Room 313', 19, 19),  ('Lab 1', 20, 20),      ('Room 501', 1, 2),
-- ('Room 502', 2, 3),    ('Room 503', 3, 4),      ('Auditorium E', 4, 5),
-- ('Room 504', 5, 6),    ('Room 505', 6, 7),      ('Lab 4', 7, 8),
-- ('Room 506', 8, 9),    ('Room 507', 9, 10),     ('Auditorium F', 10, 1);


-- ¾ Предмети (Subjects)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор предмета.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва предмета.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE SUBJECTS (
--     ID SERIAL PRIMARY KEY NOT NULL,
--     NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO SUBJECTS (NAME) VALUES
-- ('Introduction to Artificial Intelligence'),
-- ('Mathematical Analysis I'),
-- ('Organic Chemistry'),
-- ('Genetics and Cell Biology'),
-- ('Human Anatomy and Cardiology'),
-- ('History of the Ancient World'),
-- ('Formal Logic and Ethics'),
-- ('Principles of Macroeconomics'),
-- ('Criminal Procedure Law'),
-- ('Basics of Robotics and Automation'),
-- ('Social Psychology'),
-- ('Introduction to Clinical Psychotherapy'),
-- ('General and Applied Linguistics'),
-- ('Strategic Risk Management'),
-- ('Urban Architecture and Design'),
-- ('Digital Journalism and Media'),
-- ('Ecology and Climate Change'),
-- ('International Geopolitics'),
-- ('Academic Painting and Drawing'),
-- ('History of World Religions');

-- ¾ Викладачі(Teachers)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- викладача.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ■ Ставка (Salary). Ставка викладача.
-- ▷ Тип даних — DECIMAL(10, 2).
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище викладача.
-- ▷ Тип даних — varchar(max).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE TEACHERS (
--     ID SERIAL PRIMARY KEY NOT NULL,
--     NAME TEXT NOT NULL,
--     SURNAME TEXT NOT NULL,
--     SALARY DECIMAL(10, 2) NOT NULL CHECK (SALARY >= 0)
-- )


-- INSERT INTO TEACHERS (NAME, SURNAME, SALARY) VALUES
-- ('Arthur', 'Pendleton', 3500.00),
-- ('Beatrice', 'Vance', 2800.50),
-- ('Charles', 'Xavier', 4100.00),
-- ('Diana', 'Prince', 3200.00),
-- ('Edward', 'Elric', 2500.00),
-- ('Fiona', 'Gallagher', 2900.00),
-- ('George', 'Costanza', 2100.75),
-- ('Helen', 'Mirren', 3800.00),
-- ('Ian', 'Malcolm', 4300.00),
-- ('Julia', 'Roberts', 3100.00),
-- ('Kevin', 'Spacey', 2700.00),
-- ('Laura', 'Croft', 3400.00),
-- ('Martin', 'Mister', 2600.00),
-- ('Nina', 'Simone', 3000.00),
-- ('Oscar', 'Wilde', 2400.00),
-- ('Peter', 'Parker', 2150.00),
-- ('Quentin', 'Tarantino', 4500.00),
-- ('Rose', 'Tyler', 2850.00),
-- ('Samuel', 'Jackson', 3700.00),
-- ('Thomas', 'Anderson', 4000.00);


-- Завдання
-- 1. Виведіть усі можливі пари рядків викладачів і груп.

-- SELECT T.NAME, T.SURNAME, G.NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON T.ID = L.TEACHER_ID
-- JOIN GROUPS_LECTURES GL ON L.ID = GL.LECTURE_ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID

-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких перевищує фонд фінансування факультету.

-- SELECT F.NAME AS FACULTY_NAME
-- FROM FACULTIES F
-- WHERE F.FINANCING < (
--     SELECT SUM(D.FINANCING)
--     FROM DEPARTMENTS D
--     WHERE D.FACULTY_ID = F.ID
-- )

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони
-- курирують.

-- SELECT C.SURNAME, G.NAME
-- FROM CURATORS C
-- JOIN GROUPS_CURATORS GC ON C.ID = GC.CURATOR_ID
-- JOIN GROUPS G ON GC.GROUP_ID = G.ID;

-- 4. Виведіть імена та прізвища викладачів, які читають лекції
-- у групі «P107».

-- SELECT T.NAME, T.SURNAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON T.ID = L.TEACHER_ID
-- JOIN GROUPS_LECTURES GL ON L.ID = GL.LECTURE_ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- WHERE G.NAME = 'AI-302';

-- 5. Виведіть прізвища викладачів і назви факультетів, на яких
-- вони читають лекції.

-- SELECT DISTINCT T.SURNAME, F.NAME
-- FROM TEACHERS T
-- JOIN LECTURES L ON T.ID = L.TEACHER_ID
-- JOIN GROUPS_LECTURES GL ON L.ID = GL.LECTURE_ID
-- JOIN GROUPS G ON GL.GROUP_ID = G.ID
-- JOIN DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID
-- JOIN FACULTIES F ON D.FACULTY_ID = F.ID

-- 6. Виведіть назви кафедр і назви груп, які до них належать.

-- SELECT D.NAME, G.NAME
-- FROM DEPARTMENTS D
-- JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID


-- 7. Виведіть назви предметів, які викладає викладач «Samantha
-- Adams».

-- SELECT DISTINCT S.NAME AS SUBJECT_NAME
-- FROM SUBJECTS S
-- JOIN LECTURES L ON S.ID = L.SUBJECT_ID
-- JOIN TEACHERS T ON L.TEACHER_ID = T.ID
-- WHERE T.NAME = 'SAMANTHA' AND T.SURNAME = 'ADAMS'

-- 8. Виведіть назви кафедр, на яких викладається дисципліна
-- «Database Theory».

-- SELECT DISTINCT D.NAME AS DEPARTMENT_NAME
-- FROM DEPARTMENTS D
-- JOIN GROUPS G ON D.ID = G.DEPARTMENT_ID
-- JOIN GROUPS_LECTURES GL ON G.ID = GL.GROUP_ID
-- JOIN LECTURES L ON GL.LECTURE_ID = L.ID
-- JOIN SUBJECTS S ON L.SUBJECT_ID = S.ID
-- WHERE S.NAME = 'DATABASE THEORY'

-- 9. Виведіть назви груп, що належать до факультету «Computer
-- Science»

-- SELECT G.NAME AS GROUP_NAME
-- FROM GROUPS G
-- JOIN DEPARTMENTS D ON G.DEPARTMENT_ID = D.ID
-- JOIN FACULTIES F ON D.FACULTY_ID = F.ID
-- WHERE F.NAME = 'COMPUTER SCIENCE'
