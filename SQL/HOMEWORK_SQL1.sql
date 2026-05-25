-- Завдання 1
-- Створіть базу даних під назвою Birds. Розташування залишається на ваш вибір.
-- Завдання 2
-- Переназвіть базу даних із першого завдання. Нове ім’я
-- для бази даних Cats.
-- Завдання 3
-- Видаліть базу даних Cats.

-- (БУЛО ЗРОБЛЕНО POSTGRES БАЗІ ДАННИХ)

-- CREATE DATABASE BIRDS

-- ALTER DATABASE BIRDS RENAME TO "CATS"

-- DROP DATABASE "CATS"

-- CREATE DATABASE FRUITS_VEGETABLES





-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис

-- CREATE TABLE PRODUCTS(
-- 	ID SERIAL,
-- 	NAME VARCHAR(30),
-- 	TYPE VARCHAR(30),
-- 	COLOR VARCHAR(10),
-- 	CALORIES INT,
-- 	DESCRIPTION VARCHAR(100)
-- );

-- Створіть наступні запити для таблиці з інформацією про
-- овочі та фрукти із попереднього завдання:

-- INSERT INTO PRODUCTS (NAME, TYPE, COLOR, CALORIES, DESCRIPTION)
-- VALUES
-- ('Apple', 'Fruit', 'Red', 52, 'Sweet red apple'),
-- ('Banana', 'Fruit', 'Yellow', 89, 'Fresh ripe banana'),
-- ('Orange', 'Fruit', 'Orange', 47, 'Juicy orange fruit'),
-- ('Grapes', 'Fruit', 'Green', 69, 'Seedless green grapes'),
-- ('Strawberry', 'Fruit', 'Red', 33, 'Fresh sweet strawberry'),
-- ('Carrot', 'Vegetable', 'Orange', 41, 'Crunchy fresh carrot'),
-- ('Tomato', 'Vegetable', 'Red', 18, 'Ripe red tomato'),
-- ('Cucumber', 'Vegetable', 'Green', 15, 'Fresh green cucumber'),
-- ('Broccoli', 'Vegetable', 'Green', 34, 'Healthy broccoli'),
-- ('Eggplant', 'Vegetable', 'Purple', 25, 'Fresh purple eggplant');


-- ■ Відображення всієї інформації з таблиці овочів та фруктів;

-- SELECT *
-- FROM PRODUCTS;

-- ■ Відображення усіх овочів;

-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'Vegetable';

-- ■ Відображення усіх фруктів;

-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'Fruit';

-- ■ Відображення усіх назв овочів та фруктів;

-- SELECT NAME
-- FROM PRODUCTS;

-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;

-- SELECT DISTINCT COLOR
-- FROM PRODUCTS;

-- ■ Відображення фруктів певного кольору;

-- SELECT *
-- FROM PRODUCTS
-- WHERE COLOR = 'Red' AND TYPE = 'Fruit';

-- ■ Відображення овочів певного кольору.

-- SELECT *
-- FROM PRODUCTS
-- WHERE COLOR = 'Green' AND TYPE = 'Vegetable';
