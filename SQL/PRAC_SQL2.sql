-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.

-- SELECT *
-- FROM STUDENTS

-- SELECT NAME
-- FROM STUDENTS
-- WHERE 70 < MIN_MARK AND MIN_MARK < 80

-- ■ Показати інформацію про студентів, яким виповнилося 20 років.

-- ALTER TABLE STUDENTS
-- DROP COLUMN DOB

-- ALTER TABLE STUDENTS
-- ADD COLUMN BIRTHDAY DATE

-- UPDATE STUDENTS
-- SET BIRTHDAY = '2002-12-05'

-- SELECT NAME, AGE(BIRTHDAY)
-- FROM STUDENTS
-- WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) > 20

-- ■ Показати інформацію про студентів з віком, у вказаному діапазоні.
-- ■ Показати інформацію про студентів із конкретним
-- ім’ям. Наприклад, показати студентів з ім’ям Борис.

-- SELECT NAME
-- FROM STUDENTS
-- WHERE NAME ILIKE 'IVAN%'

-- ■ Показати інформацію про студентів, в номері яких
-- є три сімки.

-- SELECT *
-- FROM STUDENTS
-- WHERE PHONE ILIKE '%7%7%7%'

-- ■ Показати електронні адреси студентів, що починаються з конкретної літери.

-- SELECT *
-- FROM STUDENTS
-- WHERE EMAIL ILIKE 'M%'



-- Завдання 2
-- Створіть наступні запити для бази даних з оцінками
-- студентів із попереднього практичного завдання:
-- ■ Показати мінімальну середню оцінку по всіх студентах.

-- SELECT MIN_MARK
-- FROM STUDENTS

-- ■ Показати максимальну середню оцінку по всіх студентах.

-- SELECT MAX_MARK
-- FROM STUDENTS

-- ■ Показати статистику міст. Має відображатися назва
-- міста та кількість студентів з цього міста.
-- SELECT CITY, COUNT(*)
-- FROM STUDENTS
-- GROUP BY CITY

-- ■ Показати статистику студентів. Має відображатися
-- назва країни та кількість студентів з цієї країни.

-- SELECT COUNTRY, COUNT(*)
-- FROM STUDENTS
-- GROUP BY COUNTRY

-- ■ Показати кількість студентів з мінімальною середньою
-- оцінкою з математики.

-- SELECT COUNT(*)
-- FROM STUDENTS
-- WHERE MIN_SUBJECT = 'Math'

-- ■ Показати кількість студентів з максимальною середньою оцінкою з математики.

-- SELECT COUNT(*)
-- FROM STUDENTS
-- WHERE MAX_SUBJECT = 'Math'

-- ■ Показати кількість студентів у кожній групі.

-- SELECT GROUP_NAME, COUNT(*)
-- FROM STUDENTS
-- GROUP BY GROUP_NAME

-- ■ Показати середню оцінку групи

-- SELECT GROUP_NAME, AVG(AVG_MARK)
-- FROM STUDENTS
-- GROUP BY GROUP_NAME


-- SELECT CITY, COUNT(*)
-- FROM STUDENTS
-- GROUP BY CITY

-- SELECT *
-- FROM STUDENTS
-- WHERE AVG_MARK = (
-- 	SELECT MAX(AVG_MARK)
-- 	FROM STUDENTS
-- )


-- ВИВЕСТИ СТУДЕНТІВ ЯКІ НАВЧАЮТЬСЯ В ГРУПІ З НАЙВИЩОЮ СЕРЕДНЬОЇ ОЦІНКОЮ

-- WITH BEST_GROUP AS (
--     SELECT GROUP_NAME, AVG(AVG_MARK) AS AVG_SCORE
--     FROM STUDENTS
--     GROUP BY GROUP_NAME
-- )

-- SELECT *
-- FROM STUDENTS
-- WHERE GROUP_NAME = (
--     SELECT GROUP_NAME
--     FROM best_group
--     WHERE AVG_SCORE = (
--         SELECT MAX(avg_score)
--         FROM BEST_GROUP
--     )
-- )


-- WITH GROUP_INFO AS (
-- 	SELECT GROUP_NAME, AVG(AVG_MARK) AS GROUP_GRADE
-- 	FROM STUDENTS
-- 	GROUP BY GROUP_NAME
-- )

-- SELECT GROUP_NAME, GROUP_GRADE
-- FROM GROUP_INFO
-- WHERE GROUP_GRADE = (
-- 	SELECT MAX(GROUP_GRADE)
-- 	FROM GROUP_INFO
-- )
