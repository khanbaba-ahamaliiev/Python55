-- CREATE TABLE STUDENTS(
-- 	ID SERIAL,
-- 	NAME VARCHAR(50),
-- 	CITY VARCHAR(30),
-- 	COUNTRY VARCHAR(30),
-- 	DOB INT,
-- 	EMAIL VARCHAR(50),
-- 	PHONE VARCHAR(12),
-- 	GROUP_NAME VARCHAR(20),
-- 	AVG_MARK INT,
-- 	MIN_MARK INT,
-- 	MAX_MARK INT,
-- 	MIN_SUBJECT VARCHAR(20),
-- 	MAX_SUBJECT VARCHAR(20)
-- )


-- INSERT INTO STUDENTS
-- (NAME, CITY, COUNTRY, DOB, EMAIL, PHONE, GROUP_NAME, AVG_MARK, MIN_MARK, MAX_MARK, MIN_SUBJECT, MAX_SUBJECT)
-- VALUES
-- ('Ivan Petrenko', 'Warsaw', 'Poland', 2001, 'ivan.petrenko@gmail.com', '380671112233', 'CS-101', 85, 60, 98, 'Physics', 'Math'),
-- ('Olena Shevchenko', 'Berlin', 'Germany', 2000, 'olena.s@gmail.com', '380501234567', 'CS-102', 91, 72, 100, 'History', 'Programming'),
-- ('Maksym Kovalenko', 'Prague', 'Czech Republic', 2002, 'maksym.k@gmail.com', '380931112244', 'CS-103', 77, 55, 89, 'Math', 'English'),
-- ('Anna Bondarenko', 'Paris', 'France', 2001, 'anna.b@gmail.com', '380661223344', 'CS-101', 88, 69, 97, 'Chemistry', 'Biology'),
-- ('Dmytro Melnyk', 'Rome', 'Italy', 1999, 'dmytro.m@gmail.com', '380731334455', 'CS-104', 73, 50, 90, 'Physics', 'Sport'),
-- ('Sofia Tkachenko', 'Madrid', 'Spain', 2003, 'sofia.t@gmail.com', '380991223355', 'CS-102', 95, 80, 100, 'History', 'Programming'),
-- ('Andrii Marchenko', 'Vienna', 'Austria', 2000, 'andrii.m@gmail.com', '380671445566', 'CS-103', 82, 61, 96, 'English', 'Math'),
-- ('Kateryna Lysenko', 'Amsterdam', 'Netherlands', 2002, 'kateryna.l@gmail.com', '380501556677', 'CS-101', 90, 75, 99, 'Physics', 'Programming'),
-- ('Yurii Hnatenko', 'Brussels', 'Belgium', 2001, 'yurii.h@gmail.com', '380931667788', 'CS-104', 69, 45, 84, 'Chemistry', 'History'),
-- ('Iryna Savchenko', 'Lisbon', 'Portugal', 1998, 'iryna.s@gmail.com', '380661778899', 'CS-102', 87, 70, 98, 'Math', 'English'),

-- ('Roman Koval', 'Budapest', 'Hungary', 2002, 'roman.k@gmail.com', '380731889900', 'CS-103', 79, 58, 92, 'Physics', 'Programming'),
-- ('Viktoria Polishchuk', 'Stockholm', 'Sweden', 2001, 'viktoria.p@gmail.com', '380991990011', 'CS-101', 93, 76, 100, 'History', 'Math'),
-- ('Bohdan Oliinyk', 'Oslo', 'Norway', 2000, 'bohdan.o@gmail.com', '380672101122', 'CS-104', 71, 49, 85, 'Biology', 'Sport'),
-- ('Mariia Kravets', 'Copenhagen', 'Denmark', 1999, 'mariia.k@gmail.com', '380502202233', 'CS-102', 89, 68, 97, 'Chemistry', 'English'),
-- ('Taras Yaremchuk', 'Dublin', 'Ireland', 2003, 'taras.y@gmail.com', '380932303344', 'CS-103', 84, 62, 95, 'Math', 'Programming'),
-- ('Alina Honchar', 'Helsinki', 'Finland', 2002, 'alina.h@gmail.com', '380663404455', 'CS-101', 92, 73, 100, 'Physics', 'Math'),
-- ('Denys Shapoval', 'Athens', 'Greece', 2001, 'denys.s@gmail.com', '380734505566', 'CS-104', 76, 57, 88, 'History', 'Sport'),
-- ('Polina Vasylenko', 'Zurich', 'Switzerland', 2000, 'polina.v@gmail.com', '380995606677', 'CS-102', 94, 81, 100, 'Chemistry', 'Programming'),
-- ('Oleksii Danylko', 'Munich', 'Germany', 1998, 'oleksii.d@gmail.com', '380676707788', 'CS-103', 68, 40, 83, 'English', 'Math'),
-- ('Veronika Chorna', 'Milan', 'Italy', 2002, 'veronika.c@gmail.com', '380507808899', 'CS-101', 86, 65, 96, 'Biology', 'Programming'),

-- ('Mykhailo Sydorenko', 'Barcelona', 'Spain', 2001, 'mykhailo.s@gmail.com', '380938909900', 'CS-104', 81, 59, 94, 'Physics', 'English'),
-- ('Yana Tereshchenko', 'Hamburg', 'Germany', 2003, 'yana.t@gmail.com', '380669000111', 'CS-102', 97, 84, 100, 'History', 'Programming'),
-- ('Serhii Bezruk', 'Krakow', 'Poland', 1999, 'serhii.b@gmail.com', '380730101222', 'CS-103', 72, 50, 87, 'Math', 'Sport'),
-- ('Anastasiia Romanenko', 'Venice', 'Italy', 2000, 'anastasiia.r@gmail.com', '380991202333', 'CS-101', 91, 74, 99, 'Chemistry', 'English'),
-- ('Vitalii Hrytsenko', 'Lyon', 'France', 2002, 'vitalii.h@gmail.com', '380672303444', 'CS-104', 75, 52, 89, 'Physics', 'Math'),
-- ('Diana Kostenko', 'Nice', 'France', 2001, 'diana.k@gmail.com', '380503404555', 'CS-102', 88, 67, 97, 'History', 'Programming'),
-- ('Artem Zaharchenko', 'Valencia', 'Spain', 1998, 'artem.z@gmail.com', '380934505666', 'CS-103', 80, 60, 93, 'English', 'Sport'),
-- ('Tetiana Klymenko', 'Geneva', 'Switzerland', 2003, 'tetiana.k@gmail.com', '380665606777', 'CS-101', 96, 85, 100, 'Biology', 'Math'),
-- ('Yevhen Moroz', 'Brno', 'Czech Republic', 2000, 'yevhen.m@gmail.com', '380736707888', 'CS-104', 74, 51, 86, 'Chemistry', 'Programming'),
-- ('Kristina Pavlenko', 'Cologne', 'Germany', 2001, 'kristina.p@gmail.com', '380997808999', 'CS-102', 89, 70, 98, 'Physics', 'English'),

-- ('Ostap Chernenko', 'Naples', 'Italy', 2002, 'ostap.c@gmail.com', '380678909111', 'CS-103', 78, 56, 91, 'Math', 'Programming'),
-- ('Nadiia Bilous', 'Seville', 'Spain', 1999, 'nadiia.b@gmail.com', '380509010222', 'CS-101', 90, 71, 99, 'History', 'Biology'),
-- ('Volodymyr Tkach', 'Rotterdam', 'Netherlands', 2001, 'volodymyr.t@gmail.com', '380930111333', 'CS-104', 70, 46, 84, 'Physics', 'Sport'),
-- ('Ilona Horbach', 'Antwerp', 'Belgium', 2000, 'ilona.h@gmail.com', '380661212444', 'CS-102', 93, 78, 100, 'English', 'Programming'),
-- ('Ruslan Zadorozhnyi', 'Salzburg', 'Austria', 2003, 'ruslan.z@gmail.com', '380732313555', 'CS-103', 83, 63, 95, 'Chemistry', 'Math'),
-- ('Liliia Boiko', 'Florence', 'Italy', 2002, 'liliia.b@gmail.com', '380993414666', 'CS-101', 95, 82, 100, 'History', 'English'),
-- ('Pavlo Karpov', 'Leipzig', 'Germany', 2001, 'pavlo.k@gmail.com', '380674515777', 'CS-104', 67, 42, 81, 'Biology', 'Sport'),
-- ('Inna Fedorenko', 'Porto', 'Portugal', 2000, 'inna.f@gmail.com', '380505616888', 'CS-102', 87, 69, 96, 'Math', 'Programming'),
-- ('Oleksandr Rudyk', 'Luxembourg', 'Luxembourg', 1998, 'oleksandr.r@gmail.com', '380936717999', 'CS-103', 79, 58, 90, 'Physics', 'English'),
-- ('Halyna Kushnir', 'Edinburgh', 'United Kingdom', 2002, 'halyna.k@gmail.com', '380667818000', 'CS-101', 92, 77, 100, 'Chemistry', 'Programming');



-- SELECT *
-- FROM STUDENTS

-- SELECT NAME
-- FROM STUDENTS;

-- SELECT AVG_MARK
-- FROM STUDENTS;

-- SELECT NAME, MIN_MARK
-- FROM STUDENTS
-- WHERE MIN_MARK > 65;

-- SELECT DISTINCT COUNTRY
-- FROM STUDENTS

-- SELECT DISTINCT CITY
-- FROM STUDENTS

-- SELECT DISTINCT GROUP_NAME
-- FROM STUDENTS

-- SELECT DISTINCT MIN_SUBJECT, MIN_MARK
-- FROM STUDENTS

-- SELECT *
-- FROM STUDENTS
-- WHERE CITY = 'Brno' or CITY = 'Rome' or CITY = 'Milan'

-- СТУДЕНТИ З СЕРЕДНІМ БАЛОМ МІЖ 70 ТА 80
-- SELECT *
-- FROM STUDENTS
-- WHERE 70 < AVG_MARK AND AVG_MARK < 80

-- SELECT *
-- FROM STUDENTS
-- WHERE AVG_MARK BETWEEN 70 AND 80

-- ВИВЕСТИ ИМЯ МАКСИМАЛЬНУ ТА МІНІМАЛЬНУ ОЦІНКУ ТА РІЗНИЦЮ МІЖ НИМИ
-- SELECT NAME, MIN_MARK, MAX_MARK, MAX_MARK - MIN_MARK AS DIFF, CITY
-- FROM STUDENTS

-- SELECT DISTINCT COUNTRY
-- FROM STUDENTS

--ВИВЕСТИ ЛЮДЕЙ ЩО ЖИВУТ В ПОЛЬЩУ АБО СЕРЕДНЯ ОЦІНКА БІЛЬША ЗА 70

-- SELECT COUNTRY, AVG_MARK
-- FROM STUDENTS
-- WHERE COUNTRY = 'Poland' OR AVG_MARK > 85

-- SELECT NAME, MIN_MARK, MAX_MARK
-- FROM STUDENTS
-- WHERE MAX_MARK > MIN_MARK

-- SELECT NAME, MAX_MARK, MIN_MARK, MAX_MARK - MIN_MARK AS DIFF
-- FROM STUDENTS
-- WHERE MAX_MARK - MIN_MARK > 30

-- SELECT COUNTRY, LOWER(COUNTRY)
-- FROM STUDENTS

-- SELECT NAME
-- FROM STUDENTS
-- WHERE LOWER(COUNTRY) = 'poland'

-- SELECT NAME
-- FROM STUDENTS
-- WHERE LENGTH(NAME) > 15
