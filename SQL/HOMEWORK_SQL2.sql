-- SELECT *
-- FROM PRODUCTS


-- Завдання 1
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Відображення усіх овочів з калорійністю, менше вказаної.

-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'Vegetable' AND CALORIES < 40

-- ■ Відображення усіх фруктів з калорійністю у вказаному
-- діапазоні.

-- SELECT *
-- FROM PRODUCTS
-- WHERE TYPE = 'Fruit' AND (CALORIES BETWEEN 30 AND 60)

-- ■ Відображення усіх овочів, у назві яких є вказане слово.
-- Наприклад, слово: капуста.

-- SELECT *
-- FROM PRODUCTS
-- WHERE NAME ILIKE '%APPLE%'

-- ■ Відображення усіх овочів та фруктів, у короткому описі
-- яких є вказане слово. Наприклад, слово: гемоглобін.

-- SELECT *
-- FROM PRODUCTS
-- WHERE DESCRIPTION ILIKE '%FRESH%'

-- ■ Показати усі овочі та фрукти жовтого або червоного
-- кольору

-- SELECT *
-- FROM PRODUCTS
-- WHERE COLOR = 'Yellow' OR COLOR = 'Red'


-- Завдання 2
-- Створіть наступні запити для бази даних з інформацією
-- про овочі та фрукти з попереднього домашнього завдання:
-- ■ Показати кількість овочів.

-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE TYPE = 'Vegetable'

-- ■ Показати кількість фруктів.

-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE TYPE = 'Fruit'

-- ■ Показати кількість овочів та фруктів заданого кольору.

-- SELECT COUNT(*)
-- FROM PRODUCTS
-- WHERE COLOR = 'Yellow'

-- ■ Показати кількість овочів та фруктів кожного кольору.

-- SELECT COLOR, COUNT(*)
-- FROM PRODUCTS
-- GROUP BY COLOR

-- ■ Показати колір мінімальної кількості овочів та фруктів.

-- SELECT COLOR, COUNT(*)
-- FROM PRODUCTS
-- GROUP BY COLOR
-- ORDER BY COUNT(*)

-- ■ Показати колір максимальної кількості овочів та фруктів.

-- SELECT COLOR, COUNT(*)
-- FROM PRODUCTS
-- GROUP BY COLOR
-- ORDER BY COUNT(*) DESC

-- ■ Показати мінімальну калорійність овочів та фруктів.

-- SELECT MIN(CALORIES)
-- FROM PRODUCTS

-- ■ Показати максимальну калорійність овочів та фруктів
-- SELECT MAX(CALORIES)
-- FROM PRODUCTS
