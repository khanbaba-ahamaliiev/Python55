--  Відділення (Departments)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор відділення.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, в якому знаходиться
-- відділення.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5
-- ■ Фінансування (Financing). Фонд фінансування відділення.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 0.
-- ▷ Значення за замовчуванням — 0.
-- ■ Назва (Name). Назва відділення.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE DEPARTMENTS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(1 < BUILDING AND BUILDING < 5),
-- 	FINANCING INT NOT NULL CHECK(FINANCING >= 0) DEFAULT 0,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE
-- )

-- INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME)
-- VALUES
-- (2, 120000, 'Cardiology'),
-- (3, 95000, 'Neurology'),
-- (4, 110000, 'Surgery'),
-- (2, 87000, 'Pediatrics'),
-- (3, 76000, 'Oncology'),
-- (4, 99000, 'Traumatology'),
-- (2, 65000, 'Dermatology'),
-- (3, 83000, 'Gynecology'),
-- (4, 72000, 'Ophthalmology'),
-- (2, 105000, 'Intensive Care');


-- Захворювання (Diseases)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- захво-рювання.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Назва (Name). Назва захворювання.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Ступінь тяжкості (Severity). Ступінь тяжкості захворювання.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення
-- ▷ Не може бути менше, ніж 1.
-- ▷ Значення за замовчуванням — 1

-- CREATE TABLE DISEASES(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	SEVERITY INT NOT NULL CHECK(SEVERITY >=1) DEFAULT 1
-- )


-- INSERT INTO DISEASES (NAME, SEVERITY)
-- VALUES
-- ('Influenza', 2),
-- ('Pneumonia', 4),
-- ('Diabetes', 3),
-- ('Hypertension', 3),
-- ('Asthma', 2),
-- ('Tuberculosis', 5),
-- ('Migraine', 1),
-- ('COVID-19', 4),
-- ('Bronchitis', 2),
-- ('Arthritis', 3),
-- ('Hepatitis', 4),
-- ('Appendicitis', 5),
-- ('Anemia', 2),
-- ('Chickenpox', 1),
-- ('Malaria', 5),
-- ('Depression', 3),
-- ('Epilepsy', 4),
-- ('Gastritis', 2),
-- ('Allergy', 1),
-- ('Heart Failure', 5);


-- Лікарі (Doctors)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- лікаря.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Ім’я (Name). Ім’я лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.
-- ■ Телефон(Phone). Телефонний номер лікаря.
-- ▷ Тип даних — char(10).
-- ▷ Може містити null-значення.
-- ■ Ставка (Salary). Ставка лікаря.
-- ▷ Тип даних для зберігання грошових значень.
-- ▷ Не містить null-значення.
-- ▷ Не може бути меншою або дорівнювати 0.
-- ■ Прізвище (Surname). Прізвище лікаря.
-- ▷ Тип даних — varchar(255).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожнє.

-- CREATE TABLE DOCTORS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	NAME VARCHAR(255) NOT NULL,
-- 	PHONE CHAR(10),
-- 	SALARY INT NOT NULL CHECK(SALARY >= 0),
-- 	SURNAME VARCHAR(255) NOT NULL
-- )

-- INSERT INTO DOCTORS (NAME, PHONE, SALARY, SURNAME)
-- VALUES
-- ('Oleksandr', '0501234567', 45000, 'Shevchenko'),
-- ('Iryna', '0672345678', 52000, 'Bondarenko'),
-- ('Maksym', '0933456789', 61000, 'Tkachenko'),
-- ('Sofiia', '0994567890', 47000, 'Koval'),
-- ('Andrii', '0665678901', 70000, 'Melnyk'),
-- ('Kateryna', '0686789012', 54000, 'Savchenko'),
-- ('Dmytro', '0977890123', 63000, 'Hrytsenko'),
-- ('Olena', '0958901234', 49000, 'Marchenko'),
-- ('Yaroslav', '0639012345', 72000, 'Lysenko'),
-- ('Nataliia', '0730123456', 51000, 'Kravchenko'),
-- ('Artem', '0961234501', 58000, 'Polishchuk'),
-- ('Anastasiia', '0502345612', 46000, 'Tymoshenko'),
-- ('Ivan', '0673456723', 67000, 'Boiko'),
-- ('Viktoriia', '0934567834', 55000, 'Oliinyk'),
-- ('Petro', '0995678945', 73000, 'Klymenko'),
-- ('Alina', '0666789056', 48000, 'Romanenko'),
-- ('Serhii', '0687890167', 64000, 'Mazur'),
-- ('Mariia', '0978901278', 53000, 'Danylенко'),
-- ('Bohdan', '0959012389', 69000, 'Yaremchuk'),
-- ('Tetiana', '0630123490', 50000, 'Kostenko');

-- Обстеження (Examinations)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор
-- обсте-ження.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ День тижня (DayOfWeek). День тижня, коли проводиться обстеження.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 7.
-- ■ Час завершення (EndTime). Час завершення обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути більше, ніж час початку обстеження.
-- ■ Назва (Name). Назва обстеження.
-- ▷ Тип даних — varchar(100).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.
-- ■ Час початку (StartTime). Час початку обстеження.
-- ▷ Тип даних для зберігання часу.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 8:00 до 18:00.

-- CREATE TABLE EXAMINATIONS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	DAYOFWEEK INT NOT NULL CHECK(1 <= DAYOFWEEK AND DAYOFWEEK <=7),
-- 	ENDTIME TIME NOT NULL CHECK(ENDTIME >STARTTIME),
-- 	NAME VARCHAR(100) NOT NULL UNIQUE,
-- 	STARTTIME TIME NOT NULL CHECK('8:00' <= STARTTIME AND STARTTIME <= '18:00')
-- )


-- INSERT INTO EXAMINATIONS (DAYOFWEEK, STARTTIME, ENDTIME, NAME)
-- VALUES
-- (1, '08:00', '09:00', 'Blood Test'),
-- (1, '09:30', '10:30', 'Urine Analysis'),
-- (1, '11:00', '12:00', 'X-Ray Examination'),
-- (1, '13:00', '14:00', 'MRI Scan'),
-- (1, '15:00', '16:00', 'CT Scan'),

-- (2, '08:00', '09:00', 'Ultrasound Examination'),
-- (2, '09:30', '10:30', 'Cardiogram'),
-- (2, '11:00', '12:00', 'Eye Examination'),
-- (2, '13:00', '14:00', 'Hearing Test'),
-- (2, '15:00', '16:00', 'Allergy Test'),

-- (3, '08:00', '09:00', 'Endoscopy'),
-- (3, '09:30', '10:30', 'Colonoscopy'),
-- (3, '11:00', '12:00', 'Heart Ultrasound'),
-- (3, '13:00', '14:00', 'Stress Test'),
-- (3, '15:00', '16:00', 'Bone Density Scan'),

-- (4, '08:00', '09:00', 'Neurological Examination'),
-- (4, '09:30', '10:30', 'Dermatology Check'),
-- (4, '11:00', '12:00', 'Dental Examination'),
-- (4, '13:00', '14:00', 'Pulmonary Function Test'),
-- (4, '15:00', '16:00', 'Blood Pressure Monitoring'),

-- (5, '08:00', '09:00', 'Pregnancy Ultrasound'),
-- (5, '09:30', '10:30', 'Thyroid Examination'),
-- (5, '11:00', '12:00', 'Hormone Test'),
-- (5, '13:00', '14:00', 'Diabetes Screening'),
-- (5, '15:00', '16:00', 'Cholesterol Test'),

-- (6, '08:00', '09:00', 'Vaccination Check'),
-- (6, '09:30', '10:30', 'Skin Allergy Screening'),
-- (6, '11:00', '12:00', 'Physical Examination'),
-- (6, '13:00', '14:00', 'Cancer Screening'),
-- (7, '10:00', '11:00', 'Routine Medical Checkup');


-- Палати (Wards)
-- ■ Ідентифікатор (Id). Унікальний ідентифікатор.
-- ▷ Тип даних — int.
-- ▷ Автоприріст.
-- ▷ Не містить null-значення.
-- ▷ Первинний ключ.
-- ■ Корпус (Building). Номер корпусу, де знаходиться
-- палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Має бути в діапазоні від 1 до 5.
-- ■ Поверх (Floor). Номер поверху, на якому
-- знаходиться палата.
-- ▷ Тип даних — int.
-- ▷ Не містить null-значення.
-- ▷ Не може бути менше, ніж 1.
-- ■ Назва (Name). Назва палати.
-- ▷ Тип даних — varchar(20).
-- ▷ Не містить null-значення.
-- ▷ Не може бути порожньою.
-- ▷ Має бути унікальною.

-- CREATE TABLE WARDS(
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BUILDING INT NOT NULL CHECK(BUILDING BETWEEN 1 AND 5),
-- 	FLOOR INT NOT NULL CHECK( FLOOR >= 1),
-- 	NAME VARCHAR(20) NOT NULL UNIQUE
-- )


-- INSERT INTO WARDS (BUILDING, FLOOR, NAME)
-- VALUES
-- (1, 1, 'Ward A101'),
-- (1, 2, 'Ward A201'),
-- (1, 3, 'Ward A301'),
-- (1, 4, 'Ward A401'),

-- (2, 1, 'Ward B101'),
-- (2, 2, 'Ward B201'),
-- (2, 3, 'Ward B301'),
-- (2, 4, 'Ward B401'),

-- (3, 1, 'Ward C101'),
-- (3, 2, 'Ward C201'),
-- (3, 3, 'Ward C301'),
-- (3, 4, 'Ward C401'),

-- (4, 1, 'Ward D101'),
-- (4, 2, 'Ward D201'),
-- (4, 3, 'Ward D301'),
-- (4, 4, 'Ward D401'),

-- (5, 1, 'Ward E101'),
-- (5, 2, 'Ward E201'),
-- (5, 3, 'Ward E301'),
-- (5, 4, 'Ward E401');

-- SELECT *
-- FROM DOCTORS

-- Завдання 2
-- Для бази даних «Таблиця» створіть такі запити:
-- 1. Вивести вміст таблиці палат.

-- SELECT *
-- FROM WARDS

-- 2. Вивести прізвища та телефони усіх лікарів.

-- SELECT SURNAME, PHONE
-- FROM DOCTORS

-- 3. Вивести усі поверхи без повторень, де розміщуються
-- палати.

-- SELECT DISTINCT FLOOR
-- FROM WARDS

-- 4. Вивести назви захворювань під назвою « Name of
-- Disease» та ступінь їхньої тяжкості під назвою «Severity
-- of Disease».

-- SELECT NAME AS "NAME OF DISEASE", SEVERITY AS "SEVERITY OF DISEASE"
-- FROM DISEASES

-- 5. Вивести назви відділень, які знаходяться у корпусі 5
-- з фондом фінансування меншим, ніж 30000.

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING = 4 AND FINANCING < 90000

-- 6. Вивести назви відділень, які знаходяться у корпусі 3 з
-- фондом фінансування у діапазоні від 12000 до 15000.

-- SELECT NAME
-- FROM DEPARTMENTS
-- WHERE BUILDING = 3 AND FINANCING BETWEEN 70000 AND 90000

-- 8. Вивести назви палат, які знаходяться у корпусах 4 та
-- 5 на 1-му поверсі.

-- SELECT NAME, BUILDING, FLOOR
-- FROM WARDS
-- WHERE BUILDING BETWEEN 4 AND 5 AND FLOOR = 1

-- 9. Вивести назви, корпуси та фонди фінансування відділень, які знаходяться у корпусах 3 або 6 та мають
-- фонд фінансування менший, ніж 11000 або більший
-- за 25000.

-- SELECT NAME, BUILDING, FINANCING
-- FROM DEPARTMENTS
-- WHERE (FINANCING < 80000 OR FINANCING > 100000) AND (BUILDING = 3 OR BUILDING = 4)

-- 10. Вивести прізвища лікарів, зарплата (сума ставки та
-- надбавки 120) яких перевищує 1500.

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY + 12000 < 80000

-- 11. Вивести прізвища лікарів, у яких половина зарплати
-- перевищує триразову надбавку у вигляді 500.

-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY > 500 * 3

-- 12. Вивести назви обстежень без повторень, які проводяться у перші три дні тижня з 12:00 до 15:00.

-- SELECT DISTINCT NAME, STARTTIME, DAYOFWEEK
-- FROM EXAMINATIONS
-- WHERE (DAYOFWEEK BETWEEN 1 AND 3) AND (STARTTIME BETWEEN '12:00' AND '15:00')

-- 13. Вивести назви та номери корпусів відділень, які знаходяться у корпусах 1, 3, 8 або 10.

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1, 3, 8,10)

-- 14. Вивести назви захворювань усіх ступенів тяжкості,
-- крім 1-го та 2-го.

-- SELECT NAME, SEVERITY
-- FROM DISEASES
-- WHERE SEVERITY NOT IN (1,2)

-- 15. Вивести назви відділень, які не знаходяться у
-- першому або третьому корпусі.

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING NOT IN (1,3)

-- 16. Вивести назви відділень, які знаходяться у першому
-- або третьому корпусі.

-- SELECT NAME, BUILDING
-- FROM DEPARTMENTS
-- WHERE BUILDING IN (1,3)

-- 17. Вивести прізвища лікарів, що починаються з літери
-- «N»

-- SELECT SURNAME
-- FROM DOCTORS
-- WHERE SURNAME ILIKE 'K%'


-- Вивести кількість палат у кожному корпусі.

-- SELECT BUILDING, COUNT(BUILDING)
-- FROM WARDS
-- GROUP BY BUILDING

-- Вивести кількість палат на кожному поверсі.

-- SELECT FLOOR, COUNT(FLOOR)
-- FROM WARDS
-- GROUP BY FLOOR

-- Вивести середній фонд фінансування для кожного корпусу.

-- SELECT BUILDING, AVG(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING
-- ORDER BY BUILDING

-- Вивести максимальний фонд фінансування серед відділень у кожному корпусі.

-- SELECT BUILDING, MAX(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести мінімальний фонд фінансування серед відділень у кожному корпусі.

-- SELECT BUILDING, MIN(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести загальну суму фінансування для кожного корпусу.

-- SELECT BUILDING, SUM(FINANCING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести кількість відділень у кожному корпусі.

-- SELECT BUILDING, COUNT(BUILDING)
-- FROM DEPARTMENTS
-- GROUP BY BUILDING

-- Вивести кількість захворювань для кожного ступеня тяжкості.

-- SELECT SEVERITY, COUNT(SEVERITY)
-- FROM DISEASES
-- GROUP BY SEVERITY

-- Вивести середню зарплату лікарів залежно від наявності телефону.

-- SELECT AVG(SALARY)
-- FROM DOCTORS
-- GROUP BY PHONE IS NULL

-- Вивести середню зарплату лікарів у кожному корпусі.
-- Вивести максимальну зарплату лікарів у кожному корпусі.
-- Вивести кількість обстежень для кожного дня тижня.

-- SELECT DAYOFWEEK, COUNT(*)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найраніший час початку обстежень для кожного дня тижня.

-- SELECT DAYOFWEEK, MIN(STARTTIME)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести найпізніший час завершення обстежень для кожного дня тижня.

-- SELECT DAYOFWEEK, MAX(ENDTIME)
-- FROM EXAMINATIONS
-- GROUP BY DAYOFWEEK
-- ORDER BY DAYOFWEEK

-- Вивести кількість лікарів із зарплатою понад 2000 у кожному корпусі.



-- SELECT SURNAME, SALARY
-- FROM DOCTORS
-- WHERE SALARY = (
-- 	SELECT MAX(SALARY)
-- 	FROM DOCTORS
-- )


-- SELECT SURNAME,SALARY
-- FROM DOCTORS
-- WHERE SALARY = (
-- 	SELECT MIN(SALARY)
-- 	FROM DOCTORS
-- )


-- SELECT SURNAME,SALARY
-- FROM DOCTORS
-- WHERE SALARY > (
-- 	SELECT AVG(SALARY)
-- 	FROM DOCTORS
-- )


-- SELECT MIN(STARTTIME)
-- FROM EXAMINATIONS
